from pyeasytries import __version__
from pyeasytries import Trie
from pyeasytries.TrieNode import TrieNode
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_add():
    """
    this test function tests if the add function will return True when adding a new word
    """
    trie = Trie()
    assert ((trie.add("hello")) == True)

def test_add_existing_word():
    """
    this test function tests if the add function will return False when adding an existing word
    """
    trie = Trie()
    trie.add("hello")
    assert ((trie.add("hello")) == False)

def test_add_word_is_string():
    """
    this test function tests if the add function will give a TypeError when inserting something other than a string 
    """
     trie = Trie()  
     with pytest.raises(TypeError):
         trie.add(23)

def test_add_empty_string():
    """
    this test function tests if the add function will give a ValueError when inserting an empty string
    """
     trie = Trie()       
     with pytest.raises(ValueError):
         trie.add("")

def test_add_sucessfully_add_word():
    """
    this test function tests if the add function will correctly add the word 
    """
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
    """
    this test function tests if the add function will correctly create a new node when adding a word 
    """
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
    """
    this test function tests if the add function will correctly add a word to an existing child node
    """
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
