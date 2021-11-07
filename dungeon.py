from pico2d import *

class Dungeon:
    def __init__(self):
        self.image = load_image('던전5(600).png')

    def draw(self):
        self.image.draw(400, 300)
