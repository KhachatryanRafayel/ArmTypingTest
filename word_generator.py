"""word_generator.py

Module for filtering and saving English words to text files.

This script uses the 'wordfreq' library to get the top 5000 most frequent English words
and classifies them into three lists by length and position in the frequency ranking.
It then writes each list to a separate .txt file.

Functions:
    save_words_to_file(file_path, words): Writes a list of words to a text file (one per line).

Files created:
    - words1.txt: Common short words (2–5 characters).
    - words2.txt: Mid-frequency words (4–8 characters).
    - words3.txt: Less common longer words (6–15 characters).
"""

from wordfreq import top_n_list

# Get the top 5000 English words by frequency
all_words_list = top_n_list('en', 5000)

# Filter words by frequency and length
words1 = {word for word in all_words_list[10:2000] if 1 < len(word) < 6 and "'" not in word}
words2 = {word for word in all_words_list[2000:3500] if 3 < len(word) < 9}
words3 = {word for word in all_words_list[3500:5000] if 5 < len(word) < 16}

def save_words_to_file(file_path: str, words: set) -> None:
    """
    Saves a list of words to a text file, one word per line.

    Args:
        file_path (str): The path to the output .txt file.
        words (list of str): List of words to write.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

# Save the filtered word lists to separate files
save_words_to_file('words/words1.txt', words1)
save_words_to_file('words/words2.txt', words2)
save_words_to_file('words/words3.txt', words3)