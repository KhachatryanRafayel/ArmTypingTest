from time import time

class time_manager:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.playing_duration = 15

    def update_start_time(self, elapsed_time_nullify=False):
        
        self.start_time = time()
        if elapsed_time_nullify: self.elapsed_time = 0

    def update_elapsed_time(self):
        self.elapsed_time = int(time()-self.start_time)
        self.remaining_time = str(15-self.elapsed_time)

    def time_is_up(self): return self.elapsed_time>=self.playing_duration
