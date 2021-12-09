from pico2d import *

import game_framework
import game_world
import server
import collision

TIME_PER_ACTION = 1.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Stone:
    image = None

    def __init__(self):
        if Stone.image == None:
            Stone.image = load_image('attack_spritesheet.png')
        self.x = server.boss1.x + 30
        self.y = server.boss1.y - 80
        self.frame = 0
        self.frame_0 = 0
        self.frame_1 = 0
        self.height = 123
        self.attack_sound = load_wav('dimensionalpolice_startwave.wav')
        self.attack_sound.set_volume(32)
        self.shotgun_sound = load_wav('dimensionalpolice_shotgun.wav')
        self.shotgun_sound.set_volume(6)
        self.count = 0

    def shotgun(self):
        self.shotgun_sound.play(1)

    def get_bb(self):
        return self.x-130, self.y - 80, self.x + 100, self.y + 50

    def draw(self):
        self.image.clip_draw(self.frame_0, 0, self.frame_1, self.height, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % 16
        if self.frame >= 0 and self.frame < 1:
            self.frame_0 = 159
            self.frame_1 = 84
        elif self.frame >= 1 and self.frame < 2:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 2 and self.frame < 3:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 3 and self.frame < 4:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 4 and self.frame < 5:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 5 and self.frame < 6:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 6 and self.frame < 7:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 7 and self.frame < 8:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 8 and self.frame < 9:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 9 and self.frame < 10:
            self.frame_0 = self.frame_0 + 159
        elif self.frame >= 10 and self.frame < 11:
            self.frame_0 = 1590 + 171
            self.frame_1 = 171
            self.height = 123
        elif self.frame >= 11 and self.frame < 12:
            self.frame_0 = self.frame_0 + 208
            self.frame_1 = 208
            self.height = 142
        elif self.frame >= 12 and self.frame < 13:
            self.frame_0 = self.frame_0 + 248
            self.frame_1 = 248
            self.height = 167
        elif self.frame >= 13 and self.frame < 14:
            self.frame_0 = self.frame_0 + 268
            self.frame_1 = 268
            self.height = 189
        elif self.frame >= 14 and self.frame < 15:
            self.frame_0 = self.frame_0 + 275
            self.frame_1 = 275
            self.height = 174
        elif self.frame >= 15 and self.frame < 16:
            self.frame_0 = self.frame_0 + 286
            self.frame_1 = 286
            self.height = 185

        if self.frame >= 15:
            game_world.remove_object(self)