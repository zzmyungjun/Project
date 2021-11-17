import random
from pico2d import *
import game_framework

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Npc1:
    image = None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def __init__(self):
        if Npc1.image == None:
            Npc1.image = load_image('Npc1_sprite.png')
        self.x, self.y = 400, 334
        self.frame = 0

    def draw(self):
        self.image.clip_draw((int(self.frame) * 64), 0, 64, 64, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 49