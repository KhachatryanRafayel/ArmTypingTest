from random import shuffle

def load_words_from_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read().splitlines()
    
words1 = load_words_from_file('words/words1.txt')
shuffle(words1)
words2 = load_words_from_file('words/words2.txt')
shuffle(words2)
words3 = load_words_from_file('words/words3.txt')
shuffle(words3)

