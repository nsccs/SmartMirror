from datetime import datetime

"""
    :author Luan Ta
    Query the system's Date and Time
"""


def get_time():
    return '[size=20][font=fonts/IndieFlower-Regular.ttf]Date: ' \
        + str(datetime.now().month).zfill(2) + '/' + str(datetime.now().day).zfill(2) \
        + '/' + str(datetime.now().year) + '[/font][/size]' + '\n' \
        + 'Time: ' + str(datetime.now().hour) + ':' + str(datetime.now().minute).zfill(2) \
        + ':' + str(datetime.now().second).zfill(2)
