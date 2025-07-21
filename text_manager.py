"""
Module for managing the display and tracking of typed words in a typing speed game.

Classes:
- text_manager: Handles word display, input tracking, performance metrics (WPM/CPM), and rendering.
"""

from screen_text import screen_text
from random import shuffle
from word_loader import words1, words2, words3
from screen_image import screen_image

class text_manager:
    """
    Manages game logic for displaying and verifying typed words in a typing game.
    
    Attributes:
    - words: List of words based on difficulty level.
    - showing_words: List of screen_text objects currently visible on screen.
    - cpm_place / wpm_place: Visual containers for CPM and WPM metrics.
    - words_count: Number of words currently processed.
    - user_input: The text entered by the player.
    - edge: Right boundary limit for showing words.
    - wpm / cpm: Current words per minute and characters per minute metrics.
    - written_words_count / written_symbol_count: Counters for typed performance.
    """

    def __init__(self, difficulty = 2, center=(640, 420)):
        """
        Initialize the text manager with word difficulty and center position.

        Parameters:
        - difficulty (int): Level from 1 (easy) to 3 (hard).
        - center (tuple): Center position for displaying text.
        """
        if difficulty==1: self.words=words1
        elif difficulty==2: self.words=words2
        elif difficulty==3: self.words=words3
        self.showing_words = [screen_text(self.words[0])]
        self.cpm_place = screen_image('images/cpm_rect.png', c = (640,160))
        self.wpm_place = screen_image('images/cpm_rect.png', c = (840,160))
        self.words_count = 1
        self.user_input = ''
        self.edge = 1150
        self.wpm, self.cpm = '   ', '   '
        self.written_words_count = 0
        self.written_symbol_count = 0

    def update_showing_words(self):
        """
        Add new words to screen until the edge limit is reached.
        """
        while self.showing_words[-1].rect.right<=self.edge: 
            word_in_screen = screen_text(self.words[self.words_count])
            self.showing_words.append(word_in_screen)
            self.showing_words[-1].rect.left = self.showing_words[-2].rect.right+10
            self.words_count += 1

    def add_symbol(self, char):
        """
        Add a typed character to the user's input.
        
        Use this inside the event loop.

        Parameters:
        - char (str): A single character to append.
        """
        self.user_input = self.user_input+char

    def del_symbol(self):
        """
        Remove the last character from the user's input.
        
        Use this inside the event loop.
        """
        self.user_input = self.user_input[0:-1]

    def is_entered_word_correct(self):
        return self.user_input==self.showing_words[0].text
    
    def delete_entered_word(self):
        """
        Process the current word as typed correctly, update counters and move to the next.
        """
        self.written_symbol_count+=len(self.showing_words[0].text)
        self.showing_words = [self.showing_words[1]]
        self.showing_words[0].rect.center = (640,420)
        self.user_input = ''
        self.written_words_count+=1
        
    def show_all_elements(self, surf, elapsed_time):
        """
        Display words, input, and CPM/WPM on the screen.

        Parameters:
        - surf (pygame.Surface): Surface to draw on.
        - elapsed_time (float): Time passed since game start (in seconds).
        """
        user_text = screen_text(self.user_input, cent=(640, 520))
        user_text.show(surf)
        for word in self.showing_words:
            word.show(surf)
        try:
            self.wpm = str(round(60*self.written_words_count/(elapsed_time)))
            self.cpm = str(round(60*self.written_symbol_count/(elapsed_time)))
        except ZeroDivisionError:
            pass
        self.wpm_text = screen_text('WPM: '+self.wpm, 30, self.wpm_place.rect.center)
        self.cpm_text = screen_text('CPM: '+self.cpm, 30, self.cpm_place.rect.center)
        self.cpm_place.show(surf)
        self.wpm_place.show(surf)
        self.cpm_text.show(surf)
        self.wpm_text.show(surf)
    
    def show_result(self,surf):
        """
        Display final WPM and CPM results.

        Parameters:
        - surf (pygame.Surface): Surface to draw on.
        """
        cpm_result_text = screen_text(f'You\'re typing at {self.cpm} characters per minute', 25)
        cpm_result_text.rect.y -= 100
        wpm_result_text = screen_text(f'And at {self.wpm} word per minute.', 25)
        wpm_result_text.rect.y = cpm_result_text.rect.y + 50
        cpm_result_text.show(surf)
        wpm_result_text.show(surf)

    def game_finish(self):
        """
        Reset state to prepare for a new game session.
        """
        self.user_input = ''
        shuffle(self.words)
        self.words_count = 1
        self.showing_words = [screen_text(self.words[0])]
        self.written_symbol_count=0
        self.written_words_count=0