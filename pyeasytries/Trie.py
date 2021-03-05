from pyeasytries.TrieNode import TrieNode


class Trie:
    """This is a conceptual class representation of a Trie
    """
    def __init__(self):
        self.root = TrieNode(is_complete_word=False, children=dict())

    def contain(self, word):
        """
        Search if a complete word is present in the trie
        Parameters
        ----------
        word : The complete word to search 
            A String
   
        Returns
        -------
        Boolean indicating if the word is present in the trie
        
        Examples
        --------
        >>> from TrieNode import TrieNode
        >>> trie = Trie()
        >>> trie.contain("hello")
        TRUE
        """
        raise NotImplementedError()

    @staticmethod
    def __find_prefix__(node, words, prefix):
        """
        Private helper function for find_prefix.
        Cycles through all children of node recursively,
        adding them to words if they constitue whole words.
        """
        if node.is_complete_word:
            words.append(prefix)

        if not node.children:
            return

        for char in node.children:
            Trie.__find_prefix__(node.children[char], words, prefix + char)

    def find_prefix(self, prefix):
        """
        Finds all words that match the prefix in the trie
        Parameters
        ----------
        prefix : The prefix of the words to search for
            A String
   
        Returns
        -------
        List of words matching the prefix
        
        Examples
        --------
        >>> from TrieNode import TrieNode
        >>> trie = Trie()
        >>> trie.find_prefix("he")
        ["hello", "help", "hear"]
        """
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")

        if not prefix:
            raise ValueError("prefix must not be empty")

        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return words
            current = current.children[char]

        # Step 2: use helper function __find_prefix__
        Trie.__find_prefix__(current, words, prefix)
        return words

    def add(self, word_to_add):
        """
        Add a single word to the trie
        Parameters
        ----------
        word_to_add : The word to be added to the trie
            A String
   
        Returns
        -------
        Boolean indicating that if the insertion is successful or not. Returns false if the word is already in the trie
        
        Examples
        --------
        >>> from TrieNode import TrieNode
        >>> trie = Trie()
        >>> trie.add("firetruck")
        TRUE 
        """
        raise NotImplementedError()

    def delete(self, word_to_delete):
        """
        Deletes single word from the trie
        Parameters
        ----------
        word_to_delete : The word to be deleted from the trie
            A String
   
        Returns
        -------
        Boolean indicating that if the deletion is successful or not. Returns false if the word to delete is not in the trie
        
        Examples
        --------
        >>> from TrieNode import TrieNode
        >>> trie = Trie()
        >>> trie.delete("firetruck")
        TRUE
        """
        raise NotImplementedError()
