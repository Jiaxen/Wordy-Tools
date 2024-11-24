from collections import Counter

from src.utility import clean_word


class AnagramSolver:

    def __init__(self, word_trie):
        self.root_node = word_trie

    def generate_anagram(self, input_word):
        input_word = clean_word(input_word)
        letter_count = Counter(input_word)
        word_len = len(input_word)
        for anagram in self.generate_anagram_helper(
                letter_count, [], self.root_node, word_len
        ):
            print(anagram)

    def generate_anagram_helper(self, letter_count, builder, node, target_length):
        if node.word_end:
            if len([x for x in builder if x != " "]) >= target_length:
                yield "".join(builder)
            builder.append(" ")
            for res in self.generate_anagram_helper(
                    letter_count, builder, self.root_node, target_length
            ):
                yield res
            builder.pop()
        for letter, sub_node in node.children.items():
            if letter not in letter_count.keys() or letter_count[letter] == 0:
                continue
            letter_count[letter] -= 1
            builder.append(letter)
            for res in self.generate_anagram_helper(
                    letter_count, builder, sub_node, target_length
            ):
                yield res
            builder.pop()
            letter_count[letter] += 1
