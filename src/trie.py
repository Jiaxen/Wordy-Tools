from src.utility import clean_word


class TrieNode:

    def __init__(self, letter="", depth=0, word_end=False):
        self.letter = letter
        self.depth = depth
        self.word_end = word_end
        self.children = {}


class WordTrie:

    def __init__(self, word_list, min_word_length=3, max_word_length=20):
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.root_node = TrieNode()
        self.load_word_list(word_list)

    def load_word_list(self, path):
        with open(path, "r") as f:
            for word in f.readlines():
                word = clean_word(word)
                if self.min_word_length <= len(word) <= self.max_word_length:
                    self.load_letters(word)

    def load_letters(self, word):
        node = self.root_node
        for index, letter in enumerate(word):
            if letter not in node.children:
                node.children[letter] = TrieNode(
                    letter=letter, depth=node.depth + 1, word_end=(index == len(word) - 1)
                )
            node = node.children[letter]
