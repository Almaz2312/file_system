import shutil
from datetime import date
from pathlib import Path
from hashlib import sha256
import pickle

from hash_func import hash_string, hash_file

root = '/home/almaz/PycharmProjects/zeon/zeon_fs/.fs'


# pickle_util functions
def open_pickle(file_path):

    if not Path(file_path).exists():
        with open(Path(file_path), 'wb') as f:
            loaded: dict = {}
            pickle.dump(loaded, f)

    with open(file_path, 'rb') as f:
        loaded = pickle.load(f)

    return loaded


def pickle_dump(loaded_content, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(loaded_content, f)


# getting name and hash prefix
def get_filename(path):
    return path.split('/')[-1]


def get_hash_head(head):
    hash_prefix = "/" + '/'.join(head[:4])
    return hash_prefix


# Path related functions: Create path, get path
def create_path(file_path):
    if not Path(file_path).exists():
        Path(file_path).mkdir(parents=True, exist_ok=False)

    return file_path


def get_meta_db_path(path):
    content_hash = hash_file(path)
    hash_prefix = get_hash_head(content_hash)
    content_path = root + hash_prefix + '/meta.db'

    return content_path


def get_metadb_path_from_hash(content_hash):
    hash_prefix = get_hash_head(content_hash)
    content_path = root + hash_prefix + '/meta.db'

    return content_path


def get_names_db_path(name):
    name_hash = hash_string(name)
    hash_prefix = get_hash_head(name_hash)
    name_path = root + hash_prefix + '/names.db'

    return name_path


def get_storage_path(path):
    content_hash = hash_file(path)
    hash_prefix = get_hash_head(content_hash)
    storage_path = root + hash_prefix + '/files'
    print(storage_path)

    return storage_path


# functions related to storing files and hashes
def copy_file(source_file_path):
    shutil.copy(source_file_path, get_storage_path(source_file_path) + f'/{hash_file(source_file_path)}')


def add_content_hash(path):
    content = {
        hash_file(path):
            {
                'size': Path(path).stat().st_size,
                'files': {get_filename(path): str(date.today())}
            }
    }

    return content


def dict_filename_date(filename):
    return {filename: str(date.today())}


# def delete_name_from_meta(file_name):
