from pathlib import Path

from fs_db import check_name, check_content
from fs_utils import get_filename, copy_file, add_content_hash, get_names_db_path, get_meta_db_path, open_pickle, \
    pickle_dump, dict_filename_date, add_filename_to_trie, open_trie_pickle
from hash_func import hash_string, hash_file


def add(args):
    # check args
    if not args:
        print('Need arguments!!!')
        exit()

    # check path
    source_file_path = args[0]
    if not Path(source_file_path).exists():
        print('Path does not exists!!!')
        exit()

    filename = get_filename(source_file_path)
    if check_name(filename):
        print('Filename already exists!')
        exit()

    added_hash_name = {hash_string(filename): hash_file(source_file_path)}
    hash_names = open_pickle(get_names_db_path(filename))
    hash_names.update(added_hash_name)

    if check_content(source_file_path):
        contents = open_pickle(get_meta_db_path(source_file_path))
        contents[hash_file(source_file_path)]['files'].update(dict_filename_date(filename))

    else:
        copy_file(source_file_path)
        contents = add_content_hash(source_file_path)

    pickle_dump(contents, get_meta_db_path(source_file_path))
    pickle_dump(hash_names, get_names_db_path(filename))
    add_filename_to_trie(filename)

    print(contents, hash_names, sep='\n')
