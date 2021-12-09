from pico2d import *
from random import *
import game_world

TIME_PER_ACTION = 1.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Hand:
    image = None

    def __init__(self):
        if Hand.image == None:
            Hand.image = load_image('boss_hand_sprite.png')

        self.x, self.y = randint(200, 800), randint(100, 500)
        self.frame  = 0
        self.frame_1 = 51
        self.frame_0 = 51
        self.height = 86

    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 30

    def draw(self):
        self.image.clip_draw(self.frame_0, 0, self.frame_1, self.height, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 9
        if self.frame == 1:
            self.frame_0 = 51
            self.height = 86
            self.frame_1 = 51
        elif self.frame == 2:
            self.frame_0 = self.frame_0 + 73
            self.height = 89
            self.frame_1 = 73
        elif self.frame == 3:
            self.frame_0 = self.frame_0 + 84
            self.height = 91
            self.frame_1 = 84
        elif self.frame == 4:
            self.frame_0 = self.frame_0 + 88
            self.height = 96
            self.frame_1 = 88
        elif self.frame == 5:
            self.frame_0 = self.frame_0 + 92
            self.height = 102
            self.frame_1 = 92
        elif self.frame == 6:
            self.frame_0 = self.frame_0 + 94
            self.height = 99
            self.frame_1 = 94
        elif self.frame == 7:
            self.frame_0 = self.frame_0 + 84
            self.height = 89
            self.frame_1 = 84
        elif self.frame == 8:
            self.frame_0 = self.frame_0 + 84
            self.height = 88
            self.frame_1 = 84


        if self.frame == 0:
            game_world.remove_object(self)