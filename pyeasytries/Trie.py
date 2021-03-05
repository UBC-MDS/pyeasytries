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
        # change the input string to lowercase
        if not type(word) is str:
            raise TypeError("The input word must be a string")
        if not word.isalpha():
            raise ValueError("The input word must contain letters only")

        word = word.lower()
        node = self.root

        # check if the word is in the Trie
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        if node.is_complete_word:
            return True
        else:
            return False

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
        node = self.root

        #raise an error if input is not a string
        if type(word_to_add) != str:
            raise TypeError("The input is not a string.")
        if word_to_add == "":
            raise ValueError("The input is an empty string")

        for char in word_to_add:
            if char in node.children:
                node = node.children[char]

            else:
                new_node = TrieNode(is_complete_word=False, children=dict())
                node.children[char] = new_node
                node = new_node

        if not node.is_complete_word:
            node.is_complete_word = True
            return True

        return False

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

        delete_success, remove_link = Trie.__delete__(
            cur.children[word_to_delete[0]], word_to_delete[1:])

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
