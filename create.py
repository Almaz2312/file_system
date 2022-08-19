import os
import pathlib
import shutil

origin_file = pathlib.Path(__file__).parent / 'origin/'


def mkdir(root, data):
    return os.mkdir(root/data)


def add(root, data):
    if not pathlib.Path(origin_file / str(data)).exists():
        exit("There is no such file")
    shutil.copy(origin_file/str(data), root)
