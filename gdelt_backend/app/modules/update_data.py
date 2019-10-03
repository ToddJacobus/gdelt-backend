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

def extract_zip(input_zip):
    input_zip = zipfile.ZipFile(input_zip)
    return {i: input_zip.read(i) for i in input_zip.namelist()}

def generate_date_list(start, end):
    for d in range((end - start).days):
        yield(start + datetime.timedelta(days=d))

def generate_csv_list(dates):
    # make empty dictionary of dates to track regex results
    # csv_results = {str(d):False for d in dates} # not sure if I need this?
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

                # JUST FOR TESTING... REMOVE ME
                # SO WE DON'T HAVE TO WAIT FOR THE ENTIRE DOC TO PARSE
                        break
                    break
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    return csv_url_list #, csv_results 

def parse_data(csv_url):
    with open("field_map.json", 'r') as file:
        field_map = json.loads(file.read())
    r = requests.get(csv_url)
    if r.status_code == 200:
        with io.BytesIO() as f:
            f.write(r.content)
            extracted = extract_zip(f)
            for values in extracted.values():
                for line in values.split(b'\n'):
                    line = line.split(b'\t')
                    # for table, fields in field_map.items():
                    #     for column, indexes in fields.items():
                    #         import pdb; pdb.set_trace()
                    

                    data = {
                        table:{
                            column:[ line[indexes[0]].decode("utf-8", "replace") ] for column, indexes in fields.items()
                            if len(indexes) == 1 # just grab top level data for now...
                            } for table, fields in field_map.items()
                    }
                    import pdb; pdb.set_trace()
            


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