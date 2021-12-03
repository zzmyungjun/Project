import random
from pico2d import *
import game_framework
import server
import math
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

PIXEL_PER_METER = (30.0 / 0.6)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 3.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Slime:
    image = None

    def get_bb(self):
        if self.idle_height == 27 * 4:
            return self.x - 16, self.y - 15, self.x + 15, self.y + 15
        else:
            return self.x - 11, self.y - 10, self.x + 10, self.y + 10

    def __init__(self):
        if Slime.image == None:
            Slime.image = load_image('slime_sprite.png')
        self.x, self.y = random.randint(100, 900), random.randint(100, 600)
        self.frame = 0
        self.height = 0
        self.idle_height = 27
        self.speed = 0
        self.hp = 500
        self.timer = 1
        self.dir = random.random()*2*math.pi
        self.font = load_font('ENCR10B.TTF', 8)
        self.build_behavior_tree()

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi  # 방향을 라디안값으로 설정
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass

    def find_player(self):
        distance2 = (server.boy.x - self.x)**2 + (server.boy.y - self.y)**2
        if distance2 <= (PIXEL_PER_METER * 3) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.boy.y - self.y, server.boy.x-self.x)
        return BehaviorTree.SUCCESS

    def draw(self):
        self.image.clip_draw((int(self.frame) * 27), self.idle_height, 27, 27, self.x, self.y)
        # draw_rectangle(*self.get_bb())
        self.font.draw(self.x, self.y + 20, '(Hp: %0.0f)' % self.hp, (255, 255, 0))

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1024 - 50)
        self.y = clamp(50, self.y, 768 - 50)

    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Player',self.move_to_player)

        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        WanderChase_node = SelectorNode('WanderChase')
        WanderChase_node.add_children(chase_node, wander_node)

        self.bt = BehaviorTree(WanderChase_node)
        pass