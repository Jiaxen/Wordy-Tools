import re

def clean_word(word):  # More information
    """
    Making all letters lower case and removes all non-alphabet characters.
    """
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    return word