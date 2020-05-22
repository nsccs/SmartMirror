from datetime import datetime

"""
    :author Luan Ta
    Query the system's Date and Time
"""


def get_time():
    return str(datetime.now().month).zfill(2) + '/' + str(datetime.now().day).zfill(2) \
        + '/' + str(datetime.now().year) + '\n' \
        + 'Time: ' + str(datetime.now().hour) + ':' + str(datetime.now().minute).zfill(2) \
        + ':' + str(datetime.now().second).zfill(2)
