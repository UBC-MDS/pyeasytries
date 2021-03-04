# pyeasytries 

![](https://github.com/rainbowxyt0305/pyeasytries/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/rainbowxyt0305/pyeasytries/branch/main/graph/badge.svg)](https://codecov.io/gh/rainbowxyt0305/pyeasytries) ![Release](https://github.com/rainbowxyt0305/pyeasytries/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pyeasytries/badge/?version=latest)](https://pyeasytries.readthedocs.io/en/latest/?badge=latest)

The pyeasytries package contains classes and functions that efficiently store and search words passed by the user based on a trie data structure.

This package was developed as a project for UBC MDS-Vancouver program DSCI 524 course.

## Overview
Storing and searching words can be expensive in terms of time and computing: for example, using a balanced binary search tree, the time complexity for searching a word is $O(mlogn)$, where $m$ is the length of the word and $n$ is the number of keys in the tree. However, with the trie data structure, the time complexity for searching can be reduced to $O(m)$. The `pyeasytries` package is a simple tool to aid word insertion, deletion, and searching in the trie data structure. Users can pass any words to be stored for later-on searching or printing with certain prefix, and even modify the words in storage.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ pyeasytries
```

## Features

- `Class TrieNode`: creates a trie node.
- `Class Trie`: initializes a trie data structure with or without adding any words.

Within `Class Trie`:
- `contain(self, word)` function takes in a word and searches through the trie structure to check if it has been stored in the trie already.
- `find_prefix(self, prefix)` function takes in a prefix string and searches through the trie structure and returns a list of all words stored with the given prefix.
- `add(self, word_to_add)` function takes in a word and stores each letter of the new word in the trie data structure.
- `delete(self, word_to_delete)` function takes in a word and deletes the letters of the word if they are contained in the trie already.

## Python Ecosystem 
This `pyeasytries` package aims to simplify and speed up the process of searching through a fixed dictionary. In addition to time complexity benefits, a tries data structure also allows to search for given words inside the fixed dictionary when given a prefix. Users who are building a search/filter bar from a fixed dictionary will find this package useful! As trie is a famous data structure, there are currently some similar packages in Python such as  [pygtrie](https://pypi.org/project/pygtrie/). 

## Dependencies

Python 3.8 or greater

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://pyeasytries.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/pyeasytries/graphs/contributors).

Current contributers:
- Rachel(Yuting) Xu
- Mitchie(Yiqi) Zhao
- Kaicheng Tan
- Jordan Lau

Current collaboration strategy:
- [GitHub flow](https://guides.github.com/introduction/flow/)

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
