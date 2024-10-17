import pygame

class Timer:

    def __init__(self):
        
        self.start_time = None
        self.running = False

    def start(self):

        self.start_time = pygame.time.get_ticks()
        self.running = True

    def elapsed_time(self):

        if self.running:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000 # This will convert millieconds to seconds
            return elapsed_time
    
    def stop(self):

        self.running = False

    def reset(self):

        self.start_time = None
        self.running = False
    