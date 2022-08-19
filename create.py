import os


def mkdir(root, data):
    return os.mkdir(root/data)


def add(root, data):
    return os.mkfifo(root/data)
