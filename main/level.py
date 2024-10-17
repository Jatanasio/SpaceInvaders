import pygame


class Level:

    def __init__(self):
        self.current_level = 0

    def get_current_level(self):
        return self.current_level

    def next_level(self):

        self.current_level += 1
        return self.current_level


