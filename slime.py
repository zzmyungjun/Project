import random
from pico2d import *
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Slime:
    image = None

    def get_bb(self):
        return self.x - 11, self.y - 10, self.x + 10, self.y + 10

    def __init__(self):
        if Slime.image == None:
            Slime.image = load_image('slime_sprite.png')
        self.x, self.y = random.randint(100, 900), random.randint(100, 600)
        self.frame = 0
        self.height = 0
        self.idle_height = 27
        self.hp = 500
        self.font = load_font('ENCR10B.TTF', 8)

    def draw(self):
        self.image.clip_draw((int(self.frame) * 27), self.idle_height, 27, 27, self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x, self.y + 20, '(Hp: %0.0f)' % self.hp, (255, 255, 0))

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5