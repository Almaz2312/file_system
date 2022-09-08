from hashlib import sha256
from pathlib import Path

from fs_utils import create_path, get_hash_head, open_pickle, get_meta_db_path, get_storage_path
from hash_func import hash_string

root = '/home/almaz/PycharmProjects/zeon/zeon_fs/.fs'


def check_name(name):
    hash_name = hash_string(name)
    hash_head = sha256(name.encode()).hexdigest()[:4]
    hash_prefix = get_hash_head(hash_head)

    path = root + hash_prefix

    if not Path(path).exists():
        create_path(path)

    names = open_pickle(path + '/names.db')
    if hash_name not in names:
        return False

    return True


def check_content(path):
    hash_content = sha256(Path(path).read_bytes()).hexdigest()
    file_path = get_storage_path(path)
    content_path = get_meta_db_path(path)

    if not Path(file_path).exists():
        create_path(file_path)

    contents = open_pickle(content_path)
    if hash_content not in contents:
        return False

    return True
