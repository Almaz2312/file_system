import pathlib
import shutil
from pathlib import Path
from datetime import datetime
import pickle
from hash_func import create_dir, hash_func


def open_pickle(file_path):
    if not file_path.exists():
        with open(file_path, 'wb') as f:
            loaded: dict = {}
            pickle.dump(loaded, f)

    with open(file_path, 'rb') as f:
        loaded = pickle.load(f)

        return loaded


def add(root, data):

    # Check if file we are adding exists
    if not Path(data).exists():
        exit("There is no such file!!!")

    # Variables for better visualization and convenience in coding
    hash_name, hash_content, file_name = hash_func(data)
    name_head, name_tail = hash_name[:4], hash_name[4:]
    content_head, content_tail = hash_content[:4], hash_content[4:]

    # create a path to store hashes
    name_db = create_dir(root, name_head) / 'name.db'
    content_db = create_dir(root, content_head) / 'meta.db'
    files_dir = create_dir(root, content_head) / 'files'

    # add to name.db
    # call an open_pickle function to create if not exists and then open
    loaded_name_db = open_pickle(name_db)

    if hash_name in loaded_name_db:
        exit('File name already exists!!!')

    loaded_name_db.update({hash_name: file_name})

    with open(name_db, 'wb') as f:
        pickle.dump(loaded_name_db, f)

    print(f'Name added to --> {name_db}', 'File name added successfully!!!', loaded_name_db, sep='\n')

    # Contents info that will be appended or updated
    content = {
            hash_content: {
                'size': f'{Path(data).stat().st_size} bytes',
                'files': [{file_name: str(datetime.now().date())}]
            }
        }

    # add to content.db
    # Call a function open_pickle(data) to create file if not exists, and open it
    loaded_content = open_pickle(content_db)

    # If content_hash is in a file append to part of file
    if hash_content in loaded_content:
        print('File content already exists!!!')
        loaded_content[hash_content]['files'].append({file_name: str(datetime.now().date())})

    # if not copy original file and write whole content info
    else:
        shutil.copy(Path(data), Path(files_dir) / 'hash_content')
        loaded_content.update(content)
        print('File content updated successfully!!!')

    with open(content_db, 'wb') as f:
        pickle.dump(loaded_content, f)

    print(f'Content information added to --> {content_db}\n'
          f'File content added successfully!!!', loaded_content, sep='\n')
