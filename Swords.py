from pico2d import *

class Sword_1:
    def __init__(self):
        self.image = load_image('Sword_1.png')
        self.x = 376
        self.y = 768 // 2

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 21, self.y - 19, self.x + 19, self.y + 21

class Sword_2:
    def __init__(self):
        self.image = load_image('Sword_2.png')
        self.x = 373
        self.y = 340

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
