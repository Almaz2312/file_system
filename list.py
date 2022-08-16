import os


def dirlist(location):
    if location == 'current':
        location = os.curdir
    else:
        location = location
    return os.listdir(location)
