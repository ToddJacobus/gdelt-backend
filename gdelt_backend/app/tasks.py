from celery import shared_task

# -- local module --
from .modules.update_data import generate_csv_list, parse_data


@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def get_data(datelist):
    csv_list = generate_csv_list(datelist)
    # call data parsing functions
    # write function/module to upload data using the Django ORM
    


# chunking plan....
#   A - chunk by date:
#       - quickly generate date list syncronously
#       - pass date list into .chunks method to chunk by date.
#
#   B - chunk by csv url:
#       - syncronously generate CSV list
#       - Either use .chunk method to chunk by index of csv list,
#         or consume from a queue somehow, maybe from redis directly?
#           - the consuming from a queue would involve chaining tasks
#             then using .chunk to chunk the second task in the chain.
#             This has been difficult to do in the past...