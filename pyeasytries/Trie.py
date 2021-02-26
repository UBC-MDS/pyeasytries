from TrieNode import TrieNode


class Trie:
    """This is a conceptual class representation of a Trie

    :param word_list: List of words to be added when building the trie, can be empty
    """
    def __init__(self, word_list=None):
        raise NotImplementedError()

    def contain(self, word):
        """Search if a complete word is present in the trie

        :param word: The complete word to search
        :return: Boolean indicating if the word is present in the trie
        """
        raise NotImplementedError()

    def find_prefix(self, prefix):
        """Finds all words that match the prefix in the trie

        :param prefix: The prefix of the words to search for
        :return: List of words matching the prefix
        """
        raise NotImplementedError()

    def add(self, word_to_add):
        """Add a single word to the trie

        :param word_to_add: The word to be added to the trie
        :return: Boolean indicating that if the insertion is successful or not. Returns false if the word is already in
            the trie
        """
        raise NotImplementedError()

    def delete(self, word_to_delete):
        """Delete s single word from the trie

        :param word_to_delete: The word to be deleted from the trie
        :return: Boolean indicating that if the deletion is successful or not. Returns false if the word to delete is
            not in the trie
        """
        raise NotImplementedError()
