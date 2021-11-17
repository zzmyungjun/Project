from pico2d import *

class Shop:
    def __init__(self):
        self.image = load_image('Shop_Background.png')

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)

    def update(self):
        pass

class Background:
    def __init__(self):
        self.image = load_image('shop_backbackground.png')

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)

    def update(self):
        pass