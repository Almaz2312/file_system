from pathlib import Path

from fs_utils import open_trie_pickle, get_size_from_meta


def search(*args):

    arg = args[0]

    trie = open_trie_pickle()
    searching = trie.search(*arg)

    if not searching:
        print('No such file!!!')
        exit()

    for filename in searching:
        size = get_size_from_meta(filename)
        print(filename, f'size is: {size}')

    print(f'Quantity of files is: {len(searching)}')


def dirlist(args):
    dirs = args.split('/')

