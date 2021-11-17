from pico2d import *

class Dungeon:
    def __init__(self):
        self.image = load_image('Dungeon_Background.png')

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)

    def update(self):
        pass