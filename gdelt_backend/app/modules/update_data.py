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

def generate_date_list(start, end):
    for d in range((end - start).days):
        yield(start + datetime.timedelta(days=d))

def generate_csv_list(dates):
    # make empty dictionary of dates to track regex results
    csv_results = {d:None for d in dates}
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
                        csv_results[date] = url
                        csv_url_list.append(url)
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    import pdb; pdb.set_trace()
    return csv_results 

def parse_data(csv_url):
    pass
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