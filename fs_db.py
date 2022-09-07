import pickle
import shutil
from datetime import datetime
from pathlib import Path

from hash_func import hash_string, init_dir


def open_pickle(file_path):

    if not Path(file_path).exists():
        with open(file_path, 'wb') as f:
            loaded: dict = {}
            pickle.dump(loaded, f)

    with open(file_path, 'rb') as f:
        loaded = pickle.load(f)

    return loaded


def pickle_dump(file_path, loaded_content):
    with open(file_path, 'wb') as f:
        pickle.dump(loaded_content, f)


def add_to_name_db(root, file_path):
    # Get file name and it's hash
    hash_name, _, file_name = hash_string(file_path)

    # Get name_db file path or create it (if not exist)
    name_db = init_dir(root, hash_name) / 'name.db'

    # Open file, check file(if exists), add(if not exists)
    loaded_name_db = open_pickle(name_db)
    if hash_name in loaded_name_db:
        exit('File name already exists!!!')

    loaded_name_db.update({hash_name: file_name})
    pickle_dump(name_db, loaded_name_db)

    # Prints if successful
    print(f'Name added to --> {name_db}', 'File name added successfully!!!', loaded_name_db, sep='\n')


def add_to_content_db(root, file_path):
    # Get hash of a content and file name
    _, hash_content, file_name = hash_string(file_path)

    # Get content_db and files storage path or create(if not exists)
    content_db = init_dir(root, hash_content) / 'meta.db'
    files_storage = init_dir(root, hash_content) / 'files'

    files = {file_name: datetime.now().date()}
    content = {
        hash_content: {
            'size': f'{Path(file_path).stat().st_size} bytes',
            'files': [files]
        }
    }

    # Read a content_db file
    loaded_content_db = open_pickle(content_db)

    # If content_hash is in a file, append file name and added date
    if hash_content in loaded_content_db:
        print('File content already exists!!!')
        loaded_content_db[hash_content]['files'].append(files)

    # if not copy original file and write hash content, size, file name and added date
    else:

        shutil.copy(Path(file_path), Path(files_storage) / 'hash_content')
        loaded_content_db.update(content)
        print('File content updated successfully!!!')

    pickle_dump(content_db, loaded_content_db)

    print(f'Content information added to --> {content_db}\n'
          f'File content added successfully!!!', loaded_content_db, sep='\n')
