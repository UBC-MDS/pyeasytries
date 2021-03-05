from pyeasytries import __version__
from pyeasytries import Trie
from pyeasytries.TrieNode import TrieNode
import pytest


def test_contain_missing_word():
    trie = Trie()
    trie.root.children = {
        'a':
        TrieNode(is_complete_word=False,
                 children={
                     'c':
                     TrieNode(is_complete_word=False,
                              children={
                                  't': TrieNode(is_complete_word=True,
                                                children={})
                              }),
                     'd':
                     TrieNode(is_complete_word=True, children={})
                 })
    }
    #  root
    #   |
    #   a
    #  / \
    # c  d (complete word)
    # |
    # t (complete word)

    contain_word = trie.contain("ac")

    assert contain_word == False
    assert "a" in trie.root.children
    assert "c" in trie.root.children["a"].children
    assert not trie.root.children["a"].children["c"].is_complete_word

def test_contain_missing_word2():
    trie = Trie()
    trie.root.children = {
        'a': TrieNode(is_complete_word=False, children={
            'c': TrieNode(is_complete_word=False, children={
            't': TrieNode(is_complete_word=True, children={})
            }),
        'd': TrieNode(is_complete_word=True, children={})
        })
    }
    #  root
    #   |
    #   a
    #  / \
    # c  d (complete word)
    # |
    # t (complete word)
    
    contain_word = trie.contain("bag")

    assert contain_word == False

def test_contain_existing_word():

    trie = Trie()
    trie.root.children = {
        'a':
        TrieNode(is_complete_word=False,
                 children={
                     'c':
                     TrieNode(is_complete_word=False,
                              children={
                                  't': TrieNode(is_complete_word=True,
                                                children={})
                              }),
                     'd':
                     TrieNode(is_complete_word=True, children={})
                 })
    }
    #  root
    #   |
    #   a
    #  / \
    # c  d (complete word)
    # |
    # t (complete word)

    contain_word = trie.contain("AD")

    assert contain_word
    assert "A".lower() in trie.root.children
    assert "D".lower() in trie.root.children["a"].children
    assert trie.root.children["a"].children["d"].is_complete_word


def test_contain_report_error_on_invalid_argument_type():
    trie = Trie()

    with pytest.raises(TypeError):
        trie.contain(0)


def test_contain_report_error_on_invalid_word():
    trie = Trie()

    with pytest.raises(ValueError):
        trie.contain("6")
