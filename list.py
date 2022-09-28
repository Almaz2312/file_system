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
        print(filename)

    print('All possible directory paths')


def dirlist(args):

    #check args
    if not args:
        args = '/'

    arg = args[0]

    trie = open_trie_pickle()
    listing = trie.list(arg)
    for paths in listing:
        print(paths)

    print(f'Quantity of files is: {len(listing)}')
