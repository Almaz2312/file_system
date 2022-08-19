import os
# from main import base


def delete_directory(root, location):
    return os.rmdir(root/location)


def delete_file(root, location):
    return os.remove(root/location)