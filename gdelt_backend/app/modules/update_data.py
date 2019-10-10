import datetime
import requests
import re
import json
import zipfile
import io

## ----------------------------------------------------------
## Objectives:
##  - pass in start/end date
##  - construct date range
##  - send request to csv file master list endpoint
##  - parse through endpoints and grab url
## ----------------------------------------------------------

def debug(func):
    import traceback
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # print(e)
            traceback.print_exc()
            print(func.__name__ + " time delta: {}".format(datetime.datetime.now() - start_time))
            import pdb; pdb.set_trace()
        finally:
            print(func.__name__ + " total runtime: {}".format(datetime.datetime.now() - start_time))
        return result
    return wrapper


def extract_zip(input_zip):
    input_zip = zipfile.ZipFile(input_zip)
    return {i: input_zip.read(i) for i in input_zip.namelist()}

def generate_date_list(start, end):
    for d in range((end - start).days):
        yield(start + datetime.timedelta(days=d))

def generate_csv_list(dates):
    # make empty dictionary of dates to track regex results
    csv_url_list = []
    base_url = r"http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt"
    chunk_size = 8096
    # send request to GDELT and search for date matches
    with requests.get(base_url, stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines(chunk_size):
                url = str(line).split()[-1].strip("\'")
                for date in dates:
                    date_string = date.strftime("%Y%m%d")
                    file_regex = r"\.translation\.gkg\.csv\.zip$"
                    if re.search(date_string, url) and re.search(file_regex, url):
                        csv_url_list.append(url)

                # ----------------
                # JUST FOR TESTING... 
                # REMOVE THIS BLOCK LATER
                # SO WE DON'T HAVE TO 
                # WAIT FOR THE ENTIRE DOC TO PARSE
                        break
                    break
                # ----------------
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    return csv_url_list

def parse_data(csv_url):
    with open("field_map.json", 'r') as file:
        # See field_map.json for field:index map
        field_map = json.loads(file.read())
    r = requests.get(csv_url)
    if r.status_code == 200:
        with io.BytesIO() as f:
            f.write(r.content)
            extracted = extract_zip(f)
            for values in extracted.values():
                for line in values.split(b'\n'):
                    line = line.split(b'\t')

                    data = {}

                    ## -- Parse one-to-one fields ---------
                    data['gkg_sources'] = {}
                    for field, indexes in field_map["one-to-one"]["fields"]["gkg_sources"].items():
                        
                        if len(indexes)  == 1:
                            data['gkg_sources'][field] = line[ indexes[0] ]
                        else:
                            data['gkg_sources'][field] = line[ indexes[0] ].split(b',')[indexes[1]]


                    ## -- Parse one-to-many fields --------
                    ## NOTE: I'm sure this could be optimized somehow to reduce the number of loops
                    data['gkg_counts'] = {}
                    # TODO: add conditional to check for empty fields.
                    for field, indexes in field_map['one-to-many']['fields']['type_1']['fields']['gkg_counts'].items():
                        data['gkg_counts'][field] = [item.split(b"#")[indexes[1]] for item in line[indexes[0]].split(b';') if line[indexes[0]].split(b';')[0] ]

                    data['gkg_locations'] = {}
                    for field, indexes in field_map['one-to-many']['fields']['type_1']['fields']['gkg_locations'].items():
                        data['gkg_locations'][field] = [item.split(b"#")[indexes[1]] for item in line[indexes[0]].split(b';') if line[indexes[0]].split(b';')[0] ]

                    data['gkg_themes'] = {}
                    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_themes'].items():
                        data['gkg_themes'][field] = [item.split(b',')[ indexes[1] ] for item in line[ indexes[0] ].split(b';') if item.split(b',')[0] ]

                    data['gkg_people'] ={}
                    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_people'].items():
                        data['gkg_people'][field] = [item.split(b",")[indexes[1]] for item in line[indexes[0]].split(b';') if item.split(b',')[0] ]

                    data['gkg_orgs'] = {}
                    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_orgs'].items():
                        data['gkg_orgs'][field] = [item.split(b",")[indexes[1]] for item in line[indexes[0]].split(b';') if item.split(b',')[0] ]

                    data['gkg_images'] = {}
                    for field, indexes in field_map['one-to-many']['fields']['type_3']['fields']['gkg_images'].items():
                        data['gkg_images'][field] = [i for i in line[indexes[0]].split(b';') if line[indexes[0]].split(b';')[0] ]

                    data['GCAM'] = {}
                    for dictionary, dimension in field_map['GCAM'].items():
                        data['GCAM'][dictionary] = [d for d in dimension['dimension'][1] if d in line[dimension['dimension'][0]].split(b',')]

                    import pdb; pdb.set_trace()
                    # DEBUG: There's still some funny business going on (e.g., lon not parsed when assotiated lat is parsed),
                    #        but I think the main boilerplate is done here.
            


    else:
        print("Could not reach server.  Status code: {}".format(r.status_code))
    
    # send request to csv_url
    # chunk through response via response.iter_lines method
    # isolate and parse data elements
    # inset data elements into respective tables
        # option 1: use Django ORM
        # option 2: direct sql
        # option 3: construct csv and use COPY

if __name__ == "__main__":
    d1 = datetime.date(2018, 1, 1)
    d2 = datetime.date(2018, 2, 1)
    date_list = [d for d in generate_date_list(d1, d2)]
    csv_list = generate_csv_list(date_list)

    parse_data(csv_list[0]) # just one for testing...