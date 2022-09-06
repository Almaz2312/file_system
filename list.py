from pathlib import Path
import pickle


def dirlist(*args):

    _ = args

    files = Path(__file__).parent / 'hash_tuple.data'
    with open(files, 'rb') as files:
        loaded = pickle.load(files)

    for file in loaded:
        print(file[0], file[1], sep='\t')
