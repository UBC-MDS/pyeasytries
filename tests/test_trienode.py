import pytest

from pyeasytries import __version__
from pyeasytries.TrieNode import TrieNode


def test_version():
    assert __version__ == '0.1.0'


def test_trienode_report_error_on_invalid_is_complete_word_argument_type():
    with pytest.raises(TypeError):
        TrieNode(is_complete_word='incorrect type', children=dict())


def test_trienode_report_error_on_invalid_children_argument_type():
    with pytest.raises(TypeError):
        TrieNode(is_complete_word=False, children="string")