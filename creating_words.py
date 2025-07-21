from wordfreq import top_n_list
from random import shuffle

all_words_list = top_n_list('en', 5000)

words1 = [word for word in all_words_list[10:2000] if len(word)>1 and len(word)<6 and not "'" in word]

words2 = [word for word in all_words_list[2000:3500] if len(word)>3 and len(word)<9]

words3 = [word for word in all_words_list[3500:5000] if len(word)>5 and len(word)<16]

def save_words_to_file(file_path, words):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')
    
save_words_to_file('words/words1.txt', words1)
save_words_to_file('words/words2.txt', words2)
save_words_to_file('words/words3.txt', words3)
