import shutil
import sys
from pathlib import Path
from datetime import datetime
import pickle
from hashlib import sha256
from hash_func import create_dir


# def mkdir(root, data):
#     return os.mkdir(root/data)


# def add(root, data):
#     file = str(data).split('/').__getitem__(-1)
#     print(file)
#     file_hash_name = sha256(file).hexdigest()
#     content_hash = sha256(Path(data).read_bytes()).hexdigest()
#     # destination = root/full_hash_exten
#
#
#     # if not pathlib.Path(data).exists():
#     #     exit("There is no such file!!!")
#     #
#     # if not pathlib.Path('/home/almaz/PycharmProjects/zeon/zeon_fs/hash_tuple.data').exists():
#     #     shutil.copy(data, destination), add_hash(file, hash_func(data))
#     #     exit('Storage file created!!!')
#     #
#     # with open('/home/almaz/PycharmProjects/zeon/zeon_fs/hash_tuple.data', 'rb') as a:
#     #
#     #     load = pickle.load(a)
#     #
#     #     for item in load:
#     #
#     #         if item[0] == file:
#     #             exit('File name already exists!!!')
#     #
#     #         if hash_func(data) == item[1]:
#     #             add_hash(file, hash_func(data))
#     #             exit("File content already exists!!!")
#     #
#     #     shutil.copy(data, destination), add_hash(file, hash_func(data))
#
#     add_hash(file_hash_name)
#     add_hash(content_hash)
#
#     print('File added successfully!!!')

def add(root, data):
    file_name = str(data).split('/').__getitem__(-1)
    hash_name = sha256(file_name.encode()).hexdigest()
    hash_content = sha256(Path(data).read_bytes()).hexdigest()

    name_head, name_tail = hash_name[:4], hash_name[4:]
    content_head, content_tail = hash_content[:4], hash_content[4:]

    # create a path to store hashes

    name_db = create_dir(root, name_head) / 'name.db'
    content_db = create_dir(root, content_head) / 'meta.db'
    files_dir = create_dir(root, content_head) / 'files'

    # add to name.db
    if name_db.exists():
        with open(name_db, 'rb') as f:
            loaded = pickle.load(f)
            if hash_name in loaded:
                exit('File name already exists!!!')
        loaded.update({hash_name: file_name})
    else:
        loaded = {hash_name: file_name}

    with open(name_db, 'wb') as f:
        pickle.dump(loaded, f)

    print(f'Name added to --> {name_db}', 'File name added successfully!!!', loaded, sep='\n')

    # add to content.db
    content = {
            hash_content: {
                'size': f'{Path(data).stat().st_size} bytes',
                'files': [{file_name: str(datetime.now().date())}]
            }
        }
    # size = f'{Path(data).stat().st_size} bytes'
    # files = [{file_name: str(datetime.now().date())}]
    #
    # if not content_db.exists():
    #
    #     with open(content_db, 'wb') as f:
    #         pickle.dump({}, f)
    #
    # with open(content_db, 'rb') as f:
    #     loaded = pickle.load(f)
    #
    # if hash_content not in loaded:
    #     shutil.copy(data, files_dir/hash_content)
    #
    # loaded[hash_content] = loaded.setdefault(hash_content, {'size': size,
    #                                                         'files': []})
    #
    #
    #
    # loaded[hash_content]['files'].append({file_name: str(datetime.now().date())})

    if content_db.exists():
        with open(content_db, 'rb') as f:
            loaded = pickle.load(f)

            if hash_content in loaded:
                print('File content already exists!!!')
                loaded[hash_content]['files'].append({file_name: str(datetime.now().date())})
            else:
                loaded = loaded.update(content)
                print('File content updated successfully!!!')

    else:
        loaded = content

    with open(content_db, 'wb') as f:
        pickle.dump(loaded, f)

    print(f'Content information added to --> {content_db}', 'File content added successfully!!!', loaded, sep='\n')

