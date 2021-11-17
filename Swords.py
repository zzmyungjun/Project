from pico2d import *

class Sword_1:
    def __init__(self):
        self.image = load_image('Sword_1.png')

    def draw(self):
        self.image.draw(376, 768 // 2)

    def update(self):
        pass
