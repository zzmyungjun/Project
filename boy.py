from pico2d import *
import game_framework
import collision
import server
import game_world

PIXEL_PER_METER = (30.0 / 0.6) # 30 pixel 60cm
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.8
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Event
TOP_DOWN, BOTTOM_DOWN, RIGHT_DOWN, LEFT_DOWN, TOP_UP, BOTTOM_UP, RIGHT_UP, LEFT_UP, Z_DOWN, Z_UP= range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): TOP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): BOTTOM_DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_z): Z_DOWN,

    (SDL_KEYUP, SDLK_UP): TOP_UP,
    (SDL_KEYUP, SDLK_DOWN): BOTTOM_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_z): Z_UP
}

# class IdleState: # 가만히 서 있을때
#     def enter(boy, event):
#         if event == RIGHT_DOWN:
#             boy.velocity_x += RUN_SPEED_PPS
#             boy.height = 4
#         elif event == LEFT_DOWN:
#             boy.velocity_x -= RUN_SPEED_PPS
#             boy.height = 5
#         elif event == TOP_DOWN:
#             boy.velocity_y += RUN_SPEED_PPS
#             boy.height = 7
#         elif event == BOTTOM_DOWN:
#             boy.velocity_y -= RUN_SPEED_PPS
#             boy.height = 6
#         elif event == RIGHT_UP:
#             boy.velocity_x -= RUN_SPEED_PPS
#             boy.height = 4
#         elif event == LEFT_UP:
#             boy.velocity_x += RUN_SPEED_PPS
#             boy.height = 5
#         elif event == TOP_UP:
#             boy.velocity_y -= RUN_SPEED_PPS
#             boy.height = 7
#         elif event == BOTTOM_UP:
#             boy.velocity_y += RUN_SPEED_PPS
#             boy.height = 6
#
#     def exit(boy, event):
#         pass
#
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
#
#     def draw(boy):
#         if boy.dir_x == 0 and boy.dir_y == 0:
#             boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)
#         else:
#             boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)


class RunState: # 움직이는 상태

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += RUN_SPEED_PPS
            boy.height = 10
        elif event == LEFT_DOWN:
            boy.velocity_x -= RUN_SPEED_PPS
            boy.height = 11
        elif event == TOP_DOWN:
            boy.velocity_y += RUN_SPEED_PPS
            boy.height = 8
        elif event == BOTTOM_DOWN:
            boy.velocity_y -= RUN_SPEED_PPS
            boy.height = 9
        elif event == RIGHT_UP:
            boy.velocity_x -= RUN_SPEED_PPS
            boy.height = 4
        elif event == LEFT_UP:
            boy.velocity_x += RUN_SPEED_PPS
            boy.height = 5
        elif event == TOP_UP:
            boy.velocity_y -= RUN_SPEED_PPS
            boy.height = 7
        elif event == BOTTOM_UP:
            boy.velocity_y += RUN_SPEED_PPS
            boy.height = 6


        boy.dir_x = int(boy.velocity_x)
        boy.dir_y = int(boy.velocity_y)

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        boy.x += boy.velocity_x * game_framework.frame_time
        boy.y += boy.velocity_y * game_framework.frame_time
        boy.x = clamp(50, boy.x, 1024-50)
        boy.y = clamp(50, boy.y, 768-50)

    def draw(boy):
        if boy.velocity_x > 0:
            boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)
        elif boy.velocity_x < 0:
            boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)
        else:
            if boy.velocity_y > 0 or boy.velocity_y < 0:
                if boy.dir_y > 0:
                    boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)
                else:
                    boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)
            else: # idle 상태
                boy.image.clip_draw((int(boy.frame) % 4) * 31, boy.height * 40, 31, 40, boy.x, boy.y)

class AttackState:

    def enter(boy, event):
        if event == Z_DOWN:
            if boy.dir_x == 1:
                boy.height = 1
            elif boy.dir_x == -1:
                boy.height = 2
            elif boy.dir_y == 1:
                boy.height = 0
            else:
                boy.height = 3
        else:
            boy.height = 6

    def get_bb(boy): # 방향에 따라 if문으로 범위 조절 지금은 아래밖에 못치니까 y값 변환
        return boy.x - 15, boy.y - 17, boy.x + 10, boy.y + 18

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

    def draw(boy):
        # if boy.dir_x == 0 and boy.dir_y == 0:
        #     boy.image.clip_draw(0, boy.height * 40, 31, 40, boy.x, boy.y)
        # elif boy.dir_x == 1:
        boy.image.clip_draw(int(boy.frame) * 31, boy.height * 40, 31, 40, boy.x, boy.y)

next_state_table = {

    # IdleState: {TOP_UP: RunState, BOTTOM_UP: RunState,
    #            TOP_DOWN: RunState, BOTTOM_DOWN: RunState,
    #            RIGHT_UP: RunState, LEFT_UP: RunState,
    #            RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
    #            Z_DOWN: AttackState, Z_UP: IdleState
    #            },

    RunState: {TOP_UP: RunState, BOTTOM_UP: RunState,
               TOP_DOWN: RunState, BOTTOM_DOWN: RunState,
               RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
               Z_DOWN: AttackState, Z_UP: AttackState
               },

    AttackState: {TOP_UP: RunState, BOTTOM_UP: RunState,
               TOP_DOWN: RunState, BOTTOM_DOWN: RunState,
               RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                Z_DOWN: AttackState, Z_UP: RunState
    }
}

class Boy:

    def __init__(self):
        self.x, self.y = 1024//2, 768//2
        self.image = load_image('boy_sprite.png')
        self.font = load_font('ENCR10B.TTF', 12)
        self.dir_x = 0
        self.dir_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.frame = 0
        self.height = 6
        self.timer = 0
        self.hp = 1000
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False


    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # for slime in server.slimes:
        #     if collision.collide(server.boy, slime):

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        self.font.draw(self.x, self.y + 50, '(Hp: %0.0f)' % self.hp, (255, 255, 0))

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event((key_event))

    def get_bb(self):
        return self.x - 15, self.y - 17, self.x + 10, self.y + 18

    # def get_bb_attack(self):
    #     if self.cur_state == AttackState:
    #         return self.x - 20, self.y - 22, self.x + 20, self.y + 20
    #     else:
    #         return self.x - 15, self.y - 17, self.x + 10, self.y + 18