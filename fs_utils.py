import shutil
from datetime import date
from pathlib import Path
import pickle

from hash_func import hash_string, hash_file
from trie import ListTrieNode
from config import root, list_trie_path


def create_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


# pickle_util functions
def open_pickle(file_path):
    if not Path(file_path).exists():
        create_pickle(dict(), Path(file_path))

    with open(file_path, 'rb') as f:
        loaded = pickle.load(f)

    return loaded


def open_trie_pickle():
    if not list_trie_path.exists():
        create_pickle(ListTrieNode(), list_trie_path)

    with open(list_trie_path, 'rb') as file:
        loaded = pickle.load(file)

    return loaded


def pickle_dump(loaded_content, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(loaded_content, f)


# getting name and hash prefix
def get_filename(source_path, dest_path):
    filename = source_path.split('/')[-1]
    return dest_path + '/' + filename


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


def get_size_from_meta(filename):
    names_db_path = get_names_db_path(filename)
    file_names = open_pickle(names_db_path)
    content_hash = file_names[hash_string(filename)]
    content_db_path = get_metadb_path_from_hash(content_hash)
    content = open_pickle(content_db_path)
    size = content[content_hash]['size']

    return size


# functions related to storing files and hashes
def copy_file(source_file_path):
    shutil.copy(source_file_path, get_storage_path(source_file_path) + f'/{hash_file(source_file_path)}')


def add_content_hash(path, filename):
    content = {
        hash_file(path):
            {
                'size': Path(path).stat().st_size,
                'files': {filename: str(date.today())}
            }
    }

    return content


def dict_filename_date(filename):
    return {filename: str(date.today())}


def del_original_file(hash_content):
    prefix = get_hash_head(hash_content)
    path = root + prefix + '/files' + '/' + hash_content
    Path(path).unlink()


def add_filename_to_trie(filename, path_to):

    filenames_trie = open_trie_pickle()
    filenames_trie.add(filename, path_to)
    pickle_dump(filenames_trie, list_trie_path)


def delete_filename_from_trie(filename):
    trie = open_trie_pickle()
    trie.remove(filename)
    pickle_dump(trie, list_trie_path)

