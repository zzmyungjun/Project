from pico2d import *
import game_framework
import server

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Boss1:
    image = None

    def __init__(self):
        if Boss1.image == None:
            Boss1.image = load_image('boss1_spritesheet.png')
        self.x, self.y = 500, 350
        self.frame = 0
        self.height = 0
        self.count = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 270, int(self.height * 260), 270, 260, self.x, self.y)
        # draw_rectangle(*self.get_bb())
        # self.font.draw(self.x, self.y + 20, '(Hp: %0.0f)' % self.hp, (255, 255, 0))

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        # self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        # self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        # self.x = clamp(50, self.x, 1024 - 50)
        # self.y = clamp(50, self.y, 768 - 50)