import os
import pathlib

import hash_func
# from hash_func import remove_hash
import pickle


# def delete_directory(root, location):
#     return os.rmdir(root/location)

def delete_file(root, file_name):
    print(file_name)
    remove_hash(root, file_name)

    print("File has been deleted successfully!!!")
