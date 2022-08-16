import os


def delete_directory(location):
    return os.rmdir(location)


def delete_file(location):
    return os.remove(location)