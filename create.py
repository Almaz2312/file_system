import os


def mkdir(data):
    return os.mkdir(data)


def touch(data):
    return os.mkfifo(data)

