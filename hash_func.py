from pathlib import Path
from hashlib import sha256


def hash_string(string):
    return sha256(string.encode()).hexdigest()


def hash_file(path):
    return sha256(Path(path).read_bytes()).hexdigest()



