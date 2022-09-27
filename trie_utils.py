import pickle
from fs_utils import create_pickle, pickle_dump
from trie import ListTrieNode
from config import list_trie_path


def open_trie_pickle():
    print(list_trie_path)
    if not list_trie_path.exists():
        create_pickle(ListTrieNode(), list_trie_path)

    with open(list_trie_path, 'rb') as file:
        loaded = pickle.load(file)

    return loaded


def add_filename_to_trie(filename):

    filenames_trie = open_trie_pickle()
    filenames_trie.add(filename)
    pickle_dump(filenames_trie, list_trie_path)


def add_to_list_trie(source_file_path, dest_file_path):
    # print(f'one: {source_file_path}, two: {dest_file_path}', sep='\n')
    list_trie = open_trie_pickle()
    list_trie.add(source_file_path, dest_file_path)
    pickle_dump(list_trie, list_trie_path)


def delete_filename_from_trie(filename):
    trie = open_trie_pickle()
    trie.remove(filename)
    pickle_dump(trie, list_trie_path)