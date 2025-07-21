"""
Main module for the 'armtypingtest' typing game.

This script initializes the game window, handles the game loop,
processes events, renders elements, and manages the game states
(start, in-game, result screen).

Modules used:
- pygame: for game interface and rendering.
- sys: for exiting the application.
- screen_text: for rendering text as Pygame surfaces.
- screen_image: for displaying static image elements.
- text_manager: for word logic and word input management.
- time_manager: for time management logic.
"""

import pygame
import sys
from time_manager import time_manager
from screen_text import screen_text
from screen_image import screen_image
from text_manager import text_manager

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame_icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption('armtypingtest')

# Game state variables
is_process_going = False  # Flag indicating if game is active
written_words_count = 0   # Total words typed in session
written_symbol_count = 0  # Total characters typed in session
how_many_times_played = 0 # Session counter

# Initialize game managers
manager = text_manager(1) # Handles text generation and input processing
time_mg = time_manager()  # Manages game timing

# Load game assets
background_image = screen_image('images/background_pic.png')
# background_piece is a piece of background, that close the remaining of last word
background_piece = screen_image('images/background_piece.png')
background_piece.rect.right = background_image.rect.right - 1
background_piece.rect.y = 385

# UI elements
user_input_place = screen_image('images/user_input_place_rect.png', c=(640, 520))
main_text_place = screen_image('images/main_text_rect.png', c=(640, 420))
restart_icon = screen_image('images/restart_icon.png', c=(970, 160))
timeleft_place = screen_image('images/time_left_rect.png', c=(395, 160))
result_place = screen_image('images/result_rect.png', c=(640, 360))

def handle_game_events():
    """Processes pygame events for the main game loop.
    
    Handles:
    - Window close events
    - Keyboard input during gameplay
    - Special key processing (backspace, space)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if is_process_going and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                manager.del_symbol()
            elif event.key == pygame.K_SPACE and manager.is_entered_word_correct():
                manager.delete_entered_word()
            elif event.key != pygame.K_SPACE:
                manager.add_symbol(event.unicode)

def render_start_screen():
    """Renders the initial start screen with prompt.
    
    Displays:
    - Motivational text
    - Instruction prompt
    - Transitions to game state on any key press
    """
    screen.fill('#7a6c67')
    starting_text = screen_text('Your keyboard is waiting for the first strike... Ready?', 30, (640, 360))
    starting_text.show(screen)
    press_any_botton = screen_text('(press any button)', 25, (640, 400), (180, 159, 168))
    press_any_botton.show(screen)

    if True in pygame.key.get_pressed():
        time_mg.update_start_time()
        global is_process_going
        is_process_going = True

def render_results_screen():
    """Renders the post-game results screen.
    
    Displays:
    - Typing test results
    - Restart prompt with hover effect
    - Handles restart logic
    """
    screen.fill('#7a6c67')
    manager.show_result(screen)
    try_again_text = screen_text('Do you want to start again?', 25)
    mouse_pos = pygame.mouse.get_pos()
    
    # Hover effect
    if try_again_text.rect.inflate(20, 20).collidepoint(mouse_pos):
        pygame.draw.rect(screen, (152, 135, 128), 
                        try_again_text.rect.inflate(20, 20), 
                        border_radius=5)
        if pygame.mouse.get_pressed()[0]:
            time_mg.update_start_time(True)
            global is_process_going, written_words_count, written_symbol_count
            is_process_going = True
            written_words_count = 0
            written_symbol_count = 0
    
    try_again_text.show(screen)

def render_game_interface():
    """Renders all in-game UI elements.
    
    Includes:
    - Text input area
    - Timer display
    - Word display
    - Background elements
    """
    main_text_place.show(screen)
    user_input_place.show(screen)
    restart_icon.show(screen)
    timeleft_place.show(screen)
    
    # Update and display timer
    time_mg.update_elapsed_time()
    timeleft_text = screen_text('Time left: ' + time_mg.remaining_time, 30)
    timeleft_text.rect.center = timeleft_place.rect.center
    timeleft_text.show(screen)
    
    # Render typing content
    manager.show_all_elements(screen, time_mg.elapsed_time)
    background_piece.show(screen)

# Main game loop
while True:
    handle_game_events()
    background_image.show(screen)

    if not is_process_going:
        if not how_many_times_played:
            render_start_screen()
        else:
            render_results_screen()
    else:
        render_game_interface()
        if time_mg.time_is_up():
            manager.game_finish()
            is_process_going = False
            how_many_times_played += 1

    # Update display
    manager.update_showing_words()
    clock.tick(60)
    pygame.display.flip()