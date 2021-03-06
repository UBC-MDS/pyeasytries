import pytest

from pyeasytries import Trie
from pyeasytries.TrieNode import TrieNode


def test_prefix_not_found():
    """
    Test if the prefix the user passes in the find_prefix
        function is found in the Trie
    """
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
    """
    Test if the prefix the user passes in the find_prefix
        function is actually itself a whole word
    """
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


def test_prefix_is_string():
    """
    Test if find_prefix actually throws an error when the user
        passes in a non-string type prefix
    """
    trie = Trie()

    with pytest.raises(TypeError):
        trie.find_prefix(2021)


def test_prefix_is_empty():
    """
    Test if find_prefix actually throws an error when the user
        passes in an empty prefix
    """
    trie = Trie()

    with pytest.raises(ValueError):
        trie.find_prefix("")
