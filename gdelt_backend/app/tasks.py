from celery import shared_task

# -- local module --
from .modules.update_data import generate_csv_list, parse_data


@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def get_data(datelist):
    # currently only supporting 24hr chunks.
    # NOTE: this is only limited by the regex
    # internal to the parse_data function.

    # make list of csv's to parse from GDELT csv master list

    # NOTE:
    #   - This function needs to parse n lines from a csv file.
    #   - when n in reached, it needs to pass the chunk of n
    #     lines along for uploading.
    #   - A generator should keep track of where it is, but
    #     we need to store the object somewhere...
    #   - This might nessesitate writing a class so we can
    #     easily instantiate an object that internally keeps
    #     track.

    csv_list = generate_csv_list(datelist)
    for csv in csv_list:
        # chunk data into 10000 items lists for uploading
        data_batch = []
        batch_size = 10000
        data_generator = parse_data(csv)
        while True:
            try:
                for i in range(batch_size):
                    # parse data for each csv in list.
                    data_batch.append(next(data_generator))
                # TODO: make dis...
                upload_data(data_batch)
                data_batch = []
            except StopIteration:
                break

    
            

    # call data parsing functions
    # write function/module to upload data using the Django ORM
    


# chunking plan....
#   A - chunk by date:
#       - quickly generate date list syncronously
#       - pass date list into .chunks method to chunk by date.
#
#   A.5 - chunk by finer dates
#       - Pass in sub-24hr dates, rather than a list of days.  Since
#         each csv represents 15 minutes of data, we can chunk up to
#         15 minute intervals.
#
#   B - chunk by csv url:
#       - syncronously generate CSV list
#       - Either use .chunk method to chunk by index of csv list,
#         or consume from a queue somehow, maybe from redis directly?
#           - the consuming from a queue would involve chaining tasks
#             then using .chunk to chunk the second task in the chain.
#             This has been difficult to do in the past...