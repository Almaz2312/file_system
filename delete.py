from fs_db import check_name
from fs_utils import open_pickle, get_names_db_path, get_meta_db_path, get_metadb_path_from_hash, pickle_dump
from hash_func import hash_string


def delete_file(args):

    if not args:
        print('Need more arguments!!!')
        exit()

    file_name = args[0]
    if not check_name(file_name):
        print('There is no such file!!!')
        exit()

    names = open_pickle(get_names_db_path(file_name))
    content = names[hash_string(file_name)]
    print(names)
    names.pop(hash_string(file_name))

    contents = open_pickle(get_metadb_path_from_hash(content))
    print(contents)
    contents[content]['files'].pop(file_name)
    pickle_dump(contents, get_metadb_path_from_hash(content))
    pickle_dump(names, get_names_db_path(file_name))

    print(names, contents, "File has been deleted successfully!!!", sep='\n')
