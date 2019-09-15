from celery import shared_task

@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def get_data():
    pass
    # Get targeted URL from gdelt master file list endpoint
    # send request to csv url and iterate through chunkwise
    # get rows from csv and import to database
    # NOTE: 
    #   - if tasks depend on each other, why not make them into 
    #     a single task?
    #   - Then farm out those tasks that are themselves nessesarily
    #     asynchronous.