import pytest

from pyeasytries import Trie
from pyeasytries import __version__
from pyeasytries.TrieNode import TrieNode


def test_version():
    assert __version__ == '0.1.0'


def test_delete_correctly_delete_existing_word():
    trie = Trie()
    trie.root.children = {
        'a': TrieNode(is_complete_word=False, children={
            'd': TrieNode(is_complete_word=True, children=dict())
        })
    }
    #   root
    #    |
    #    a
    #   /
    #  d

    is_deleted = trie.delete("ad")
    # After removal, should be:
    #   root

    assert is_deleted
    assert not trie.root.children


def test_delete_correctly_not_delete_non_existing_word():
    trie = Trie()
    trie.root.children = {
        'a': TrieNode(is_complete_word=False, children={
            'd': TrieNode(is_complete_word=True, children=dict())
        })
    }
    #   root
    #    |
    #    a
    #   /
    #  d

    is_deleted = trie.delete("a")
    # Deletion should fail, and nothing should be changed

    assert not is_deleted
    assert "a" in trie.root.children
    assert "d" in trie.root.children["a"].children
    assert trie.root.children["a"].children["d"].is_complete_word


def test_delete_correctly_not_delete_non_existing_word_with_existing_prefix():
    trie = Trie()
    trie.root.children = {
        'a': TrieNode(is_complete_word=False, children={
            'd': TrieNode(is_complete_word=True, children=dict())
        })
    }
    #   root
    #    |
    #    a
    #   /
    #  d

    is_deleted = trie.delete("ax")
    # Deletion should fail, and nothing should be changed

    assert not is_deleted
    assert "a" in trie.root.children
    assert "d" in trie.root.children["a"].children
    assert trie.root.children["a"].children["d"].is_complete_word
    assert "x" not in trie.root.children["a"].children


def test_delete_correctly_delete_partial_tree_nodes():
    trie = Trie()
    trie.root.children = {
        'a': TrieNode(is_complete_word=False, children={
            'd': TrieNode(is_complete_word=True, children=dict()),
            'c': TrieNode(is_complete_word=True, children=dict())
        })
    }
    #   root
    #    |
    #    a
    #   / \
    #  d  c

    is_deleted = trie.delete("ac")
    # After removal, should be
    #   root
    #    |
    #    a
    #   /
    #  d

    assert is_deleted
    assert "a" in trie.root.children
    assert "d" in trie.root.children["a"].children
    assert trie.root.children["a"].children["d"].is_complete_word
    assert "c" not in trie.root.children["a"].children


def test_delete_correctly_delete_nested_word():
    trie = Trie()
    trie.root.children = {
        'b': TrieNode(is_complete_word=False, children={
            'e': TrieNode(is_complete_word=True, children={
                'd': TrieNode(is_complete_word=True, children=dict())
            })
        })
    }
    #   root
    #    |
    #    b
    #    \
    #     e (complete word)
    #      \
    #      d (complete word)

    is_deleted = trie.delete("be")
    #   root
    #    |
    #    b
    #    \
    #     e
    #      \
    #      d (complete word)

    assert is_deleted
    assert "b" in trie.root.children
    assert "e" in trie.root.children["b"].children
    assert not trie.root.children["b"].children["e"].is_complete_word
    assert "d" in trie.root.children["b"].children["e"].children
    assert trie.root.children["b"].children["e"].children["d"].is_complete_word


def test_delete_report_error_on_invalid_argument_type():
    trie = Trie()

    with pytest.raises(TypeError):
        trie.delete(2567)


def test_delete_report_error_on_empty_word_argument():
    trie = Trie()

    with pytest.raises(ValueError):
        trie.delete('')
