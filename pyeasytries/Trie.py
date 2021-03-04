from pyeasytries.TrieNode import TrieNode


class Trie:
    """This is a conceptual class representation of a Trie

    :param word_list: List of words to be added when building the trie, can be empty
    """
    def __init__(self, word_list=None):
        raise NotImplementedError()

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
        >>> trie.contains("hello")
        TRUE
        """
        raise NotImplementedError()

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
        raise NotImplementedError()

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
        >>> trie.word_to_add("firetruck")
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
        >>> trie.word_to_delete("firetruck")
        TRUE 
        """
        raise NotImplementedError()
