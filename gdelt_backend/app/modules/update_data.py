import datetime
import requests

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
    base_url = r"http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt"
    chunk_size = 8096
    # send request to GDELT and search for date matches
    with requests.get(base_url, stream=True) as response:
        if response.status_code = 200:
            for chunk in response.iter_lines(chunk_size):
                for date in dates: # this loop could be optimized/avoided?
                    regex = r"http://.*{y}{m}{d}\d{6}.*\.gkg\.csv\.zip".format(
                        y = date.year,
                        m = date.month,
                        d = date.day
                    )
                    matches = re.findall(regex, chunk, re.IGNORECASE)
                    if len(matches) = 1:
                        csv_results[date] = matches[0]
                    elif len(matches) > 1:
                        # this means our regex is bad... i.e., too matchy
                        raise
                    
        else:
            # could not connect to server for whatever reason...
            raise
    return csv_results