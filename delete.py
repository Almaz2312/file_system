import os
import pathlib
# from main import base


def delete_directory(root, location):
    return os.rmdir(root/location)


def delete_file(root, location):
    if not pathlib.Path(root/location).exists():
        exit('File does not exists')
    return os.remove(root/location)