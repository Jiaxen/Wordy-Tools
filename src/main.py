from src.anagram_service import AnagramSolver
from src.trie import WordTrie

WORD_LIST = 'word_list/words_simple.txt'
MIN_WORD_LEN = 5
MAX_WORD_LEN = 20

def main():
    word_trie = WordTrie(WORD_LIST, MIN_WORD_LEN, MAX_WORD_LEN)
    anagram_service = AnagramSolver(word_trie.root_node)
    while True:
        input_word = input('Find the anagram of: ')
        if not input_word:
            break
        anagram_service.generate_anagram(input_word)

if __name__ == '__main__':
    main()