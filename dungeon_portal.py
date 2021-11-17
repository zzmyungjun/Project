import random
from pico2d import *
import game_world
import game_framework

class Portal:
    image = None

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 32, self.y + 8

    def __init__(self):
        if Portal.image == None:
            Portal.image = load_image('Dungeon_Portal.png')
        self.x, self.y = 1024 // 2, 768-100

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass