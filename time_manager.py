"""
Module for managing time tracking in the typing speed game.

Classes:
- time_manager: Handles start time, elapsed time, and game duration logic.
"""

from time import time

class time_manager:
    """
    Tracks time during a typing game session.

    Attributes:
    - start_time (float): Time when the game session started.
    - elapsed_time (int): Seconds elapsed since the start.
    - playing_duration (int): Duration of the game in seconds.
    - remaining_time (str): Time left until the game ends (as string).
    """

    def __init__(self):
        """
        Initialize the time manager with default values.
        """
        self.start_time = 0
        self.elapsed_time = 0
        self.playing_duration = 5  # You can adjust this as needed

    def update_start_time(self, elapsed_time_nullify=False):
        """
        Set the current start time to the current moment.

        Parameters:
        - elapsed_time_nullify (bool): If True, reset elapsed time to zero.
        """
        self.start_time = time()
        if elapsed_time_nullify:
            self.elapsed_time = 0

    def update_elapsed_time(self):
        """
        Update the elapsed time based on the current time and start time.

        Also updates:
        - self.remaining_time (str): Seconds left as a string.
        """
        self.elapsed_time = int(time() - self.start_time)
        self.remaining_time = str(self.playing_duration - self.elapsed_time)

    def time_is_up(self):
        """
        Check if the game duration has been reached.

        Returns:
        - bool: True if time is up, False otherwise.
        """
        return self.elapsed_time >= self.playing_duration