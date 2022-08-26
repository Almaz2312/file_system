import hashlib
from pathlib import Path
import json


def hash_func(args):
    sha1 = hashlib.sha1()
    sha1.update(Path(args).read_bytes())
    return sha1.hexdigest()


def add_hash(file, data):
    fname = '/home/almaz/PycharmProjects/zeon/zeon_fs/hash_dict.json'
    a = {file: data}
    if Path(fname).exists():
        with open(fname, "r") as f:
            loaded = json.load(f)
        loaded.append(a)
    else:
        loaded = [a]

    with open(fname, "w") as f:
        json.dump(loaded, f, indent=1)

    return loaded


def remove_hash(dict_val, file_name):
    fname = '/home/almaz/PycharmProjects/zeon/zeon_fs/hash_dict.json'
    a = {file_name: dict_val}
    with open(fname, "r") as f:
        loaded = json.load(f)
        loaded.remove(a)

    with open(fname, "w") as f:
        json.dump(loaded, f, indent=1)

