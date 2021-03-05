from pyeasytries import __version__
from pyeasytries import Trie
from pyeasytries.TrieNode import TrieNode
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_add():
    trie = Trie()
    assert ((trie.add("hello")) == True)

def test_add_existing_word():
    trie = Trie()
    trie.add("hello")
    assert ((trie.add("hello")) == False)

def test_add_word_is_string():
     trie = Trie()  
     with pytest.raises(TypeError):
         trie.add(23)

def test_empty_string():
     trie = Trie()       
     with pytest.raises(ValueError):
         trie.add("")

def test_sucessfully_add_word():
    trie = Trie()

    #  root
    #    |
    #    h
    #   /
    #  e
    
    trie.add("he")
    
    assert "h" in trie.root.children
    assert "e" in trie.root.children["h"].children
    assert trie.root.children["h"].children["e"].is_complete_word

def test_add_sucessfully_creates_new_node():
    trie = Trie()

    #  root
    #    |
    #    h
    #   / \
    #  e  i

    trie.add("he")
    trie.add("hi")
    
    assert "h" in trie.root.children
    assert "i" in trie.root.children["h"].children
    assert "e" in trie.root.children["h"].children
    assert trie.root.children["h"].children["i"].is_complete_word
    assert trie.root.children["h"].children["e"].is_complete_word

def test_add_to_existing_node():
    trie = Trie()
    
    trie.add("he")
    trie.add("hed")

    #  root
    #    |
    #    h
    #   / \
    #  e  i
    #  |
    #  d
    
    assert "h" in trie.root.children
    assert "e" in trie.root.children["h"].children
    assert "d" in trie.root.children["h"].children["e"].children
    assert trie.root.children["h"].children["e"].children["d"].is_complete_word
