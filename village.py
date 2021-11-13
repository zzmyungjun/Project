from pico2d import *

class Village:
    def __init__(self):
        self.image = load_image('Village_Background.png')

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)