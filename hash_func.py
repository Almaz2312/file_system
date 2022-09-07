from pathlib import Path
from hashlib import sha256


def hash_string(data):
    name = str(data).split('/').__getitem__(-1)
    name_hash = sha256(name.encode()).hexdigest()
    content_hash = sha256(Path(data).read_bytes()).hexdigest()

    return name_hash, content_hash, name


def init_dir(root, hashes):
    hash_head = hashes[:4]

    for i in hash_head:
        root = root / i

    if not root.exists():
        Path.mkdir(root / 'files', parents=True, exist_ok=False)

    return root
