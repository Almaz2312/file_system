import os
import pathlib
import shutil


def mkdir(root, data):
    return os.mkdir(root/data)


def add(root, data):
    file = str(data).split('/').__getitem__(-1)
    print(file)
    if not pathlib.Path(data).exists():
        exit("There is no such file")

    if pathlib.Path(root / file).exists():
        exit("File already exists")

    shutil.copy(data, root)
    print('File added')