# import hashlib
import os
from pathlib import Path
import pickle


def set_path(root, hash_head):
    hash_path = root
    for item in hash_head:
        hash_path = hash_path / item

    if not hash_path.exists():
        Path.mkdir(hash_path, exist_ok=False)


def add_hash(destination, hashes):
    hash_head, hash_tail = hashes[:4], hashes[4:]

    hash_path = Path('/home/almaz/PycharmProjects/zeon/zeon_fs/.fs')

    for item in hash_head:
        hash_path = hash_path / item

    hash_path = hash_path / destination

    if not hash_path.exists():
        Path.mkdir(hash_path, exist_ok=False)

    pickle_path = hash_path / hash_head

    if pickle_path.exists():
        with open(pickle_path, 'rb') as f:
            loaded = pickle.load(f)
            if hashes in loaded:
                exit('Hash already exists!!!')
        loaded.update()

    # if Path(fname).exists():
    #     with open(fname, "rb") as f:
    #         loaded = pickle.load(f)
    #         for items in loaded:
    #             if items.keys() == file:
    #                 exit('File name already exists!!!')
    #     loaded = loaded + a
    # else:
    #     loaded = a
    #
    # with open(fname, "wb") as f:
    #     pickle.dump(loaded, f)
    #
    # return loaded


def remove_hash(root, file_name):
    exten = file_name.split('.')
    fname = '/home/almaz/PycharmProjects/zeon/zeon_fs/hash_tuple.data'
    with open(fname, "rb") as f:
        loaded = pickle.load(f)
        for items in range(len(loaded)):
            if loaded[items][0] == file_name:
                formatted_loaded = list(loaded)
                files_hash = loaded[items][1]
                file_hash_exten = files_hash + '.' + exten[-1]
                formatted_loaded.pop(items)

                if not formatted_loaded:
                    os.remove(root / file_hash_exten)
                    exit('Removed successfully!!!')

                if files_hash not in formatted_loaded[0]:
                    print(files_hash)
                    os.remove(root/file_hash_exten)

        formatted_loaded = tuple(formatted_loaded)

    with open(fname, "wb") as f:
        pickle.dump(tuple(formatted_loaded), f)


# def hash_dir(root, args):
#     file_hash = hash_func(args)
#     hash_head, hash_tail = file_hash[:4], file_hash[4:]
#     path = None
#     for item in hash_head:
#         root = root/item
#         path = Path(root)
#         if not path.exists():
#             Path.mkdir(path, exist_ok=False)
#
#     pickle_name = hash_head
#     hash_list = Path('/home/almaz/PycharmProjects/zeon/zeon_fs/') / pickle_name
#
#     return hash_list

def create_dir(root, hashes):
    hash_head, hash_tail = hashes[:4], hashes[:4]

    for i in hash_head:
        root = root / i

    if not root.exists():
        Path.mkdir(root, parents=True, exist_ok=False)

    return root
