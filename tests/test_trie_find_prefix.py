from pyeasytries import __version__
from pyeasytries.TrieNode import TrieNode
from pyeasytries import Trie


def test_version():
    assert __version__ == '0.1.0'


def test_prefix_not_found():
    trie = Trie()
    trie.root.children = {
        'b':
        TrieNode(is_complete_word=False,
                 children={
                     'a':
                     TrieNode(is_complete_word=False,
                              children={
                                  'd': TrieNode(is_complete_word=True,
                                                children={})
                              }),
                     'e':
                     TrieNode(is_complete_word=True,
                              children={
                                  'e': TrieNode(is_complete_word=True,
                                                children={})
                              })
                 })
    }
    #     root
    #      /
    #     b
    #    / \
    #   a   e
    #  /     \
    # d       e

    prefix_not_found = trie.find_prefix("ca")
    # Finding a prefix word that's not in the Trie, should return:
    # an empty list

    assert prefix_not_found == list()
    assert "b" in trie.root.children
    assert "a" in trie.root.children["b"].children
    assert trie.root.children["b"].children["e"].is_complete_word


def test_prefix_is_whole_word():
    trie = Trie()
    trie.root.children = {
        'b':
        TrieNode(is_complete_word=False,
                 children={
                     'a':
                     TrieNode(is_complete_word=False,
                              children={
                                  'd': TrieNode(is_complete_word=True,
                                                children={})
                              }),
                     'e':
                     TrieNode(is_complete_word=True,
                              children={
                                  'e': TrieNode(is_complete_word=True,
                                                children={})
                              })
                 })
    }
    #     root
    #      /
    #     b
    #    / \
    #   a   e
    #  /     \
    # d       e

    prefix_is_whole_word = trie.find_prefix("be")
    # Finding a prefix that's already a whole word, should return:
    # this word and plus any other words that start with the prefix

    assert prefix_is_whole_word == ["be", "bee"]
    assert "b" in trie.root.children
    assert "e" in trie.root.children["b"].children
    assert trie.root.children["b"].children["e"].is_complete_word