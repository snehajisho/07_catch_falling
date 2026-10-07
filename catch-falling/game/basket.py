"""
Basket: the player-controlled catcher at the bottom of the screen.
"""

import pygame

class Basket:
    def __init__(self, x, y, width=90, height=24, speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.normal_speed = speed
        self.boost_speed = speed * 2
        self.speed = self.normal_speed

        self.boosted_frames = 0

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2), int(self.y - self.height / 2),
            self.width, self.height,
        )