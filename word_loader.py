"""
Module for loading and shuffling word lists from text files.

Functions:
- load_words_from_file: Loads words from a file and returns them as a list.
- shuffle: Imported from random, used to shuffle word lists in-place.
"""

from random import shuffle

def load_words_from_file(file_path):
    """
    Loads words from a text file.

    Each line in the file is treated as a separate word.

    Parameters:
    - file_path (str): Path to the .txt file containing words.

    Returns:
    - list[str]: A list of words read from the file.
    """
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()

# Load and shuffle word lists
words1 = load_words_from_file('words/words1.txt')
shuffle(words1)

words2 = load_words_from_file('words/words2.txt')
shuffle(words2)

words3 = load_words_from_file('words/words3.txt')
shuffle(words3)