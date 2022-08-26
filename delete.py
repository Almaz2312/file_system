import os
import pathlib

import hash_func
from hash_func import remove_hash


# def delete_directory(root, location):
#     return os.rmdir(root/location)


def delete_file(root, file_name):

    print(file_name)

    if not pathlib.Path(root/file_name).exists():
        exit('File does not exists')
    path = hash_func.hash_func(root/file_name)
    os.remove(root/file_name)
    remove_hash(path, file_name)

    print("File has been deleted successfully!!!")