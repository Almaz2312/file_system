from collections import defaultdict


class ListTrieNode:
    def __init__(self, iterable=()):
        self._children = defaultdict(ListTrieNode)
        self._file = False
        for element, dest in iterable:
            self.add(element, dest)

    def add(self, path_from, path_to):
        file_name = path_from.split('/')[-1]
        path = path_to + '/' + file_name
        element = path.split('/')
        node = self
        for s in element:
            node = node._children[s]
        node._file = True

    def list(self, path):
        term = path.split('/')
        results = []
        element = []
        if term[0] == '':
            term.remove('')

        if path == '/':
            for k in self._children.keys():
                results.append(k)

        def _list(m, node, i):
            element.append(m)

            if i == len(term):
                for i, k in node._children.items():
                    element.append(i)
                    filtered = filter(lambda x: x, element)
                    results.append('/'.join(filtered))
                    element.pop()

            elif term[i] in node._children:
                _list(term[i], node._children[term[i]], i + 1)

        _list('', self, 0)
        return results

    def search(self, path):
        term = list(path.split('/'))
        result = []
        element = []

        def _search(m, node, i):
            element.append(m)

            if i == len(term):
                filtered = filter(lambda x: x, element)
                result.append('/'.join(filtered))

            elif term[i] == '?':
                for k, child in node._children.items():
                    _search(k, child, i + 1)

            elif term[i] == '*':
                _search('', node, i+1)

                for k, child in node._children.items():
                    _search(k, child, i)

            elif term[i] in node._children:
                _search(term[i], node._children[term[i]], i + 1)

            element.pop()

        _search('', self, 0)
        return result

    def remove(self, path):
        node = self
        element = path.split('/')
        for s in element:
            node = node._children[s]
        node._file = False

        def _check_nodes(self, names):
            trie = self
            for i in names[:-1]:
                trie = trie._children[i]

            node_child = trie._children[names[-1]]
            if not node_child._children and not node_child._file:
                trie._children.pop(names[-1])

            if len(names) > 1:
                _check_nodes(self, names[:-1])

        _check_nodes(self, element)
