class TrieNode:
    """This is a conceptual class representation of a single node in a trie

    :param is_complete_word: A boolean value marks if the path to this node
        forms a complete word.
    :param children: A dictionary that maps from the next alphabet to the
        corresponding sub-tree. Can be None if this node is a leaf.
    """

    def __init__(self, is_complete_word, children):
        if not isinstance(is_complete_word, bool):
            raise TypeError("is_complete_word must be of type bool")

        if not isinstance(children, dict):
            raise TypeError("children must be of type dict")

        self.children = children
        self.is_complete_word = is_complete_word
