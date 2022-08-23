import os
import pathlib
import shutil
import json

from hash_func import hash_func, add_hash


# def mkdir(root, data):
#     return os.mkdir(root/data)


def add(root, data):

    file = str(data).split('/').__getitem__(-1)
    print(file)

    if not pathlib.Path(data).exists():
        exit("There is no such file")

    if pathlib.Path(root / file).exists():
        exit("File already exists")

    add_hash(file, hash_func(data))
    with open('/home/almaz/PycharmProjects/zeon/zeon_fs/hash_dict.json', 'r') as a:
        aqw = json.load(a)
        for item in aqw:
            if hash_func(data) in item.values():
                os.symlink(pathlib.Path(data), root/file)
                exit("File content already exists")
            else:
                shutil.copy(data, root)




    # os.symlink(pathlib.Path(data), root/file)
    print('File added')
