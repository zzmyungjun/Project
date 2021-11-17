import random
from pico2d import *
import game_framework

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class House:
    image = None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def __init__(self):
        if House.image == None:
            House.image = load_image('House_sprite.png')
        self.x, self.y = 800, 124
        self.frame = 0

    def draw(self):
        self.image.clip_draw((int(self.frame) * 217), 0, 217, 156, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6