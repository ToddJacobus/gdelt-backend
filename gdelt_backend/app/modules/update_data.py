import datetime
import requests
import re

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
                        csv_results[date] = True
                        csv_url_list.append(url)
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    return csv_url_list #, csv_results 

def parse_data(csv_url):
    field_map = {
    # This field map represents the index of parsed data lines by table.
    # the first index represents the first dimension in the parsed list.
        'gkg_sources':{
            'gkg_id': 0,
            'pub_date': 1,
            'source_id': 2,
            'source_name': 3,
            'doc_uri': 4,
        # Tone Scores.. parse from V2Tone column
            'positive_score':[15, 1],
            'negative_score':[15, 2],
            'polarity':[15, 3],
            'activity_ref_density':[15, 4],
            'pronoun_ref_density':[15, 5],
            'word_count':[15, 6]
        },
        # i.e., V2Counts
        'gkg_counts':{
            'pub_date':1,
            'count_type':[6, 0],
            'count_n':[6, 1],
            'object_type':[6, 2],
            'location_type':[6, 3],
            'location_name':[6, 4],
            'location_country':[6, 5],
            'location_adm1':[6, 6],
            'location_lat':[6, 7],
            'location_lon':[6, 8],
            # Dont forget to calculate geometry...
        },
        'gkg_themes':{
            'pub_date':1,
            'theme':[8, 0],
            'text_offset':[8, 1]
        },
        'gkg_locations':{
            'pub_date':1,
            'location_type':[10, 0],
            'location_name':[10, 1],
            'location_country':[10, 2],
            'location_adm1':[10, 3],
            'location_lat':[10, 4],
            'location_lon':[10, 5],
            'location_feature_id':[10, 6],
            # don't forget to calculate geometry...
        },
        'gkg_people':{
            'pub_date':1,
            'person_name':[12, 0],
            'text_offset':[12, 1]
        },
        'gkg_orgs':{
            'pub_date':1,
            'org_name':[14, 0],
            'text_offset':[14, 1]
        },
        'gkg_liwc':{
            'pub_date':1,
            # LIWC dimensions cannot be parsed in order, since the GCAM
            # field does not contain records for all scores and also does
            # not report scores of 0.  This field needs to be parsed by 
            # matching the code below, which is 'c' (word count based), 
            # '5' (DictionaryID), 'n' (DimensionID).
            'dimension':17, [
                'c5.1',
                'c5.2',
                'c5.3',
                'c5.4',
                'c5.5',
                'c5.6',
                'c5.7',
                'c5.8',
                'c5.9',
                'c5.10',
                'c5.11',
                'c5.12',
                'c5.13',
                'c5.14',
                'c5.15',
                'c5.16',
                'c5.17',
                'c5.18',
                'c5.19',
                'c5.20',
                'c5.21',
                'c5.22',
                'c5.23',
                'c5.24',
                'c5.25',
                'c5.26',
                'c5.27',
                'c5.28',
                'c5.29',
                'c5.30',
                'c5.31',
                'c5.32',
                'c5.33',
                'c5.34',
                'c5.35',
                'c5.36',
                'c5.37',
                'c5.38',
                'c5.39',
                'c5.40',
                'c5.41',
                'c5.42',
                'c5.43',
                'c5.44',
                'c5.45',
                'c5.46',
                'c5.47',
                'c5.48',
                'c5.49',
                'c5.50',
                'c5.51',
                'c5.52',
                'c5.53',
                'c5.54',
                'c5.55',
                'c5.56',
                'c5.57',
                'c5.58',
                'c5.59',
                'c5.60',
                'c5.61',
                'c5.62',
            ],
            # This is the score that follows each dimension id above.
            # To parse this value, you'll have to identify a Dictionary.Dimension
            # id, then grab the value that follows it.
            'word_count':17
        },
        'gkg_images':{
            'pub_date':1,
            'image_url':19
        }



    }
    r = requests.get(csv_url)
    if r.status_code == 200:
        with io.BytesIO() as f:
            f.write(r.content)
            extracted = extract_zip(f)
            for data in extracted.values():
                for line in data.split(b'\n'):
                    fields = line.split(b'\t')


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