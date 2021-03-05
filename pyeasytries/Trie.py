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
        >>> trie.add("firetruck")
        TRUE 
        """
        
        raise NotImplementedError()

    @staticmethod
    def __delete__(cur, word_to_delete):
        if not word_to_delete:
            # word to delete is empty
            if cur.is_complete_word:
                cur.is_complete_word = False
                if not cur.children:
                    return True, True
                else:
                    return True, False
            else:
                return False, False

        if word_to_delete[0] not in cur.children:
            return False, False

        delete_success, remove_link = Trie.__delete__(cur.children[word_to_delete[0]], word_to_delete[1:])

        if not delete_success:
            return False, False

        if remove_link:
            del cur.children[word_to_delete[0]]

        if len(cur.children) == 0 and not cur.is_complete_word:
            return True, True
        else:
            return True, False

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
        if not isinstance(word_to_delete, str):
            raise TypeError("word_to_delete must be a string")

        if not word_to_delete:
            raise ValueError("word_to_delete must not be empty")

        delete_success, _ = Trie.__delete__(self.root, word_to_delete)
        return delete_success
