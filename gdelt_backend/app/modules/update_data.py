import datetime
import requests
import re
import json
import zipfile
import io

# -- DEBUG --
import traceback

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

def clock(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(func.__name__ + " runtime: {}".format(datetime.datetime.now() - start_time))
        with open("../../../logs/runtime.log", "a+") as file:
            
            file.write("{timestamp}: {func_name} runtime: {runtime}\n".format(
                timestamp = datetime.datetime.now(),
                func_name = func.__name__,
                runtime = datetime.datetime.now() - start_time
            ))
        return result
    return wrapper

@clock
def extract_zip(input_zip):
    input_zip = zipfile.ZipFile(input_zip)
    return {i: input_zip.read(i) for i in input_zip.namelist()}

@clock
def generate_date_list(start, end):
    for d in range((end - start).days):
        yield(start + datetime.timedelta(days=d))

@clock
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
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    return csv_url_list

def parse_line(line, field_map):
    line = line.split(b'\t')

    data = {}

    ## -- Parse one-to-one fields ---------
    data['gkg_sources'] = {}
    for field, indexes in field_map["one-to-one"]["fields"]["gkg_sources"].items():
        if line[ indexes[0] ]:
            if len(indexes)  == 1:
                data['gkg_sources'][field] = line[ indexes[0] ]
            else:
                data['gkg_sources'][field] = line[ indexes[0] ].split(b',')[indexes[1]]

    ## -- Parse one-to-many fields --------
    ## NOTE: I'm sure these functions could be optimized somehow to reduce the number of loops
    ##       For example:
    ##          - if the line does not contain data for a given field, we don't need to iterate
    ##            over every field in the field_map.
    ##          - Maybe this could be converted from loops to native parsing methods, like "split"
    ##            or to a more dedicated csv parsing library, if it exists?.

    data['gkg_counts'] = {}
    # TODO: add conditional to check for empty fields.
    for field, indexes in field_map['one-to-many']['fields']['type_1']['fields']['gkg_counts'].items():
        if line[ indexes[0] ]:
        # data['gkg_counts'][field] = [item.split(b"#")[indexes[1]] for item in line[indexes[0]].split(b';') if line[indexes[0]].split(b';')[0] ]
            data['gkg_counts'][field] = [item.split(b"#")[indexes[1]] for item in line[indexes[0]].split(b';') if item ]

    data['gkg_locations'] = {}
    for field, indexes in field_map['one-to-many']['fields']['type_1']['fields']['gkg_locations'].items():
        if line[ indexes[0] ]:
            data['gkg_locations'][field] = [item.split(b"#")[indexes[1]] for item in line[indexes[0]].split(b';') if item ]

    data['gkg_themes'] = {}
    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_themes'].items():
        if line[ indexes[0] ]:
            data['gkg_themes'][field] = [item.split(b',')[ indexes[1] ] for item in line[ indexes[0] ].split(b';') if item ]

    data['gkg_people'] ={}
    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_people'].items():
        if line[ indexes[0] ]:
            data['gkg_people'][field] = [item.split(b",")[indexes[1]] for item in line[indexes[0]].split(b';') if item]

    data['gkg_orgs'] = {}
    for field, indexes in field_map['one-to-many']['fields']['type_2']['fields']['gkg_orgs'].items():
        if line[ indexes[0] ]:
            data['gkg_orgs'][field] = [item.split(b",")[indexes[1]] for item in line[indexes[0]].split(b';') if item]

    data['gkg_images'] = {}
    for field, indexes in field_map['one-to-many']['fields']['type_3']['fields']['gkg_images'].items():
        if line[ indexes[0] ]:
            data['gkg_images'][field] = [item for item in line[indexes[0]].split(b';') if item]

    data['GCAM'] = {}
    for dictionary, dimension in field_map['GCAM'].items():
        data['GCAM'][dictionary] = [d for d in dimension['dimension'][1] if d in line[dimension['dimension'][0]].split(b',')]
    return data

@clock
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
                for line in values.strip().split(b'\n'):
                    # Execute core line parsing logic
                    data = parse_line(line, field_map)
        # yield one row of data at a time.
        yield data
    else:
        with open("../../../logs/http_errors.log", "a+") as file:
            file.write("{timestamp}: {status_code} -- {url}\n".format(
                timestame = datetime.datetime.now(),
                status_code = r.status_code,
                url = csv_url
            ))
        print("Could not reach server.  Status code: {}".format(r.status_code))

if __name__ == "__main__":
    d1 = datetime.date(2018, 1, 1)
    d2 = datetime.date(2018, 1, 2)
    # d2 = datetime.date(2018, 2, 1)
    date_list = [d for d in generate_date_list(d1, d2)]
    csv_list = generate_csv_list(date_list)

    @clock
    def get_data():
        return [[line for line in parse_data(csv)] for csv in generate_csv_list(date_list)]

    data = get_data()
    import pdb; pdb.set_trace()