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
    base_url = r"http://data.gdeltproject.org/gdeltv2/masterfilelist-translation.txt"
    chunk_size = 8096
    # send request to GDELT and search for date matches
    with requests.get(base_url, stream=True) as response:
        if response.status_code == 200:
            for chunk in response.iter_lines(chunk_size):
                for date in dates: # this loop could be optimized/avoided?
                    # DEBUG: this regex is broken...
                    #        Consider simplifying.. e.g., just split the line on whitespace and
                    #        match the date on the last item.  If matched, grab the url.
                    regex = r"http://.*" + date.strftime("%Y%m%d") + r"\d{6}.*\.gkg\.csv\.zip"
                    matches = re.findall(regex, str(chunk), re.IGNORECASE)
                    if len(matches) == 1:
                        csv_results[date] = matches[0]
                    elif len(matches) > 1:
                        # this means our regex is bad... i.e., too matchy
                        print("WARNING: Check your regex... it's too matchy.")
                    import pdb; pdb.set_trace()
                    
        else:
            # could not connect to server for whatever reason...
            print("Could not connect. Server returned a {}".format(response.status_code))
    return csv_results 

if __name__ == "__main__":
    d1 = datetime.date(2018, 1, 1)
    d2 = datetime.date(2018, 2, 1)
    date_list = [d for d in generate_date_list(d1, d2)]
    csv_list = generate_csv_list(date_list)