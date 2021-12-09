from pico2d import *

class Bossroom_1:
    def __init__(self):
        self.image = load_image('bossroom1_background.png')
        self.bgm = load_music('amazingforestmp3.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)

    def update(self):
        pass

class Bossroom_2:
    def __init__(self):
        self.image = load_image('bossroom2_background.png')

    def draw(self):
        self.image.draw(1024 // 2, 768 // 2)

    def update(self):
        pass