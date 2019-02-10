import requests

from datetime import datetime, timedelta

from .managers import CourseSyncManager


def pull_courses():
    next_page_url = "https://www.edx.org/api/v1/catalog/search?page=1&page_size=100"
    page_number = 1
    sync_manager = CourseSyncManager()

    total_request_time = timedelta()
    total_logic_time = timedelta()

    while next_page_url:
        request_start_time = datetime.now()
        data = requests.get(next_page_url).json()
        total_request_time += datetime.now() - request_start_time
        next_page_url = data['objects']['next']
        sync_operation_start_time = datetime.now()
        sync_manager.sync(data['objects']['results'])
        total_logic_time += datetime.now() - sync_operation_start_time
        page_number += 1
        print("Just finished syncing patch #{} to edx.org.. it took time: {}".format(
                page_number - 1, datetime.now() - request_start_time
            )
        )
    print("#################################################")
    print("Total time taken: {}".format(total_logic_time + total_request_time))
    print("Total request time taken: {}".format(total_request_time))
    print("Total logic time taken: {}".format(total_logic_time))
