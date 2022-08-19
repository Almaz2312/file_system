import os
import pathlib
import shutil

origin_file = pathlib.Path(__file__).parent / 'origin/'


def mkdir(root, data):
    return os.mkdir(root/data)


def add(root, data):
    if not pathlib.Path(origin_file / data).exists():
        exit("There is no such file")
    if pathlib.Path(root / data).exists():
        exit("File already exists")
    shutil.copy(origin_file/str(data), root)
