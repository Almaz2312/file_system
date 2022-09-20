from collections import defaultdict


class TrieNode:
    def __init__(self, iterable=()):
        self._children = defaultdict(TrieNode)
        self._end = False
        for element in iterable:
            self.add(element)

    def add(self, element):
        node = self
        for s in element:
            node = node._children[s]
        node._end = True

    def remove(self, element):
        node = self
        for s in element:
            node = node._children[s]
        node._end = False

        def _check_nodes(self, names):

            trie = self
            for s in names[:-1]:
                trie = trie._children[s]

            node_child = trie._children[names[-1]]
            if len(names) > 1:
                if not node_child._children and not node_child._end:
                    if len(trie._children) == 1:
                        trie._children = defaultdict(TrieNode)

            if names:
                print(names)

                _check_nodes(self, names[:-1])

        _check_nodes(self, element)

    def search(self, term):
        results = []
        element = []

        def _search(m, node, i):

            element.append(m)
            if i == len(term):
                if node._end:
                    results.append(''.join(element))

            elif term[i] == '?':
                for k, child in node._children.items():
                    _search(k, child, i + 1)
            elif term[i] == '*':
                _search('', node, i + 1)
                for k, child in node._children.items():
                    _search(k, child, i)
            elif term[i] in node._children:
                _search(term[i], node._children[term[i]], i + 1)

            element.pop()

        _search('', self, 0)
        return results

    def __iter__(self):
        return iter(self.search('*'))

    def __len__(self):
        return sum(1 for _ in self)
