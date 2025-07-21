from screenText import screen_text

from words import words1, words2, words3

class text_manager:
    def __init__(self, difficulty = 2, center=(640, 420)):
        if difficulty==1: self.words=words1
        elif difficulty==2: self.words=words2
        elif difficulty==3: self.words=words3

        
        
        
        self.showing_words = [screen_text(self.words[0])]
        
        self.words_count = 1
        self.user_input = ''
        self.edge = 1150
        self.wpm, self.cpm = '',''
        self.written_words_count = 0
        self.written_symbol_count = 0
        self.i=1
        
    
      
    
    def update_showing_words(self):
        
        while self.showing_words[-1].rect.right<=self.edge:
            
            word_in_screen = screen_text(self.words[self.words_count])
            self.showing_words.append(word_in_screen)
            self.showing_words[-1].rect.left = self.showing_words[-2].rect.right+10
            self.i+=1
            self.words_count += 1


    def add_symbol(self, char): #use only in event loop
        self.user_input = self.user_input+char

    def del_symbol(self): #use only in event loop
        self.user_input = self.user_input[0:-1]

    def is_entered_word_correct(self):
        return self.user_input==self.showing_words[0].text
    
    def delete_entered_word(self):
        # self.showing_words = self.showing_words[1:]
        self.showing_words = [self.showing_words[1]]
        self.showing_words[0].rect.center = (640,420)
        self.user_input = ''
        self.i=1
        

    def show_user_input(self, surf):
        user_text = screen_text(self.user_input, cent=(640, 520))
        user_text.show(surf)

    def show_words_for_typing(self, surf):
        for word in self.showing_words:
            word.show(surf)

    
    
if __name__ == '__main__':
    a = text_manager(difficulty=2)

