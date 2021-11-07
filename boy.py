from pico2d import *

# Boy Event
TOP_DOWN, BOTTOM_DOWN, RIGHT_DOWN, LEFT_DOWN, TOP_UP, BOTTOM_UP, RIGHT_UP, LEFT_UP, SLEEP_TIMER = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): TOP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): BOTTOM_DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,

    (SDL_KEYUP, SDLK_UP): TOP_UP,
    (SDL_KEYUP, SDLK_DOWN): BOTTOM_UP,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
}

class IdleState: # 가만히 서 있을때
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += 1
            boy.height = 0
        elif event == LEFT_DOWN:
            boy.velocity_x -= 1
            boy.height = 2
        elif event == TOP_DOWN:
            boy.velocity_y += 1
            boy.height = 1
        elif event == BOTTOM_DOWN:
            boy.velocity_y -= 1
            boy.height = 3
        elif event == RIGHT_UP:
            boy.velocity_x -= 1
        elif event == LEFT_UP:
            boy.velocity_x += 1
        elif event == TOP_UP:
            boy.velocity_y -= 1
        elif event == BOTTOM_UP:
            boy.velocity_y += 1
        # elif event == LEFT_DOWN and event == TOP_DOWN:
        #     boy.velocity_x -= 1
        #     boy.veloctiy_y += 1
        # elif event == LEFT_DOWN and event == BOTTOM_DOWN:
        #     boy.velocity_x -= 1
        #     boy.veloctiy_y -= 1
        # elif event == RIGHT_DOWN and event == TOP_DOWN:
        #     boy.velocity_x += 1
        #     boy.veloctiy_y += 1
        # elif event == RIGHT_DOWN and event == BOTTOM_DOWN:
        #     boy.velocity_x += 1
        #     boy.veloctiy_y -= 1
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 7
        boy.timer -= 1
        # if boy.timer == 0:
        #     boy.add_event(SLEEP_TIMER) # 가만히 서 있으면 SLEEP 상태로 간다.

    def draw(boy):
        if boy.velocity_x == 0 and boy.velocity_y == 0:
            delay(0.1)
            boy.image.clip_draw((boy.frame * 41) + 207, 3 * 52, 40, 52, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 41, boy.height * 52, 40, 52, boy.x, boy.y)


class RunState: # 움직이는 상태

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity_x += 1
            boy.height = 0
        elif event == LEFT_DOWN:
            boy.velocity_x -= 1
            boy.height = 2
        elif event == TOP_DOWN:
            boy.velocity_y += 1
            boy.height = 1
        elif event == BOTTOM_DOWN:
            boy.velocity_y -= 1
            boy.height = 3
        elif event == RIGHT_UP:
            boy.velocity_x -= 1
        elif event == LEFT_UP:
            boy.velocity_x += 1
        elif event == TOP_UP:
            boy.velocity_y -= 1
        elif event == BOTTOM_UP:
            boy.velocity_y += 1
        # elif event == LEFT_DOWN and event == TOP_DOWN:
        #     boy.velocity_x -= 1
        #     boy.veloctiy_y += 1
        # elif event == LEFT_DOWN and event == BOTTOM_DOWN:
        #     boy.velocity_x -= 1
        #     boy.veloctiy_y -= 1
        # elif event == RIGHT_DOWN and event == TOP_DOWN:
        #     boy.velocity_x += 1
        #     boy.veloctiy_y += 1
        # elif event == RIGHT_DOWN and event == BOTTOM_DOWN:
        #     boy.velocity_x += 1
        #     boy.veloctiy_y -= 1

        boy.dir_x = boy.velocity_x
        boy.dir_y = boy.velocity_y

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 4
        boy.timer -= 1
        boy.x += boy.velocity_x
        boy.y += boy.velocity_y
        boy.x = clamp(25, boy.x, 800-25)
        boy.y = clamp(25, boy.y, 600 - 25)

    def draw(boy):
        if boy.velocity_x == 0 and boy.velocity_y == 0:
            boy.image.clip_draw(5 * 40, 3 * 52, 40, 52, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 41, boy.height * 52, 40, 52, boy.x, boy.y)


# class SleepState:
#
#     def enter(boy, event):
#         boy.frame = 0
#
#     def exit(boy, event):
#         pass
#
#     def do(boy):
#         boy.frame = (boy.frame + 1) % 8
#
#     def draw(boy):
#         if boy.dir == 1:
#             boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
#             3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
#         else:
#             boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
#             -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


next_state_table = {
    IdleState: {TOP_UP: RunState, BOTTOM_UP: RunState,
               TOP_DOWN: RunState, BOTTOM_DOWN: RunState,
               RIGHT_UP: RunState, LEFT_UP: RunState,
               RIGHT_DOWN: RunState, LEFT_DOWN: RunState
                },

    RunState: {TOP_UP: IdleState, BOTTOM_UP: IdleState,
               TOP_DOWN: IdleState, BOTTOM_DOWN: IdleState,
               RIGHT_UP: IdleState, LEFT_UP: IdleState,
               RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState
               },

    # SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
    #              LEFT_UP: RunState, RIGHT_UP: RunState}

}

class Boy:

    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('character_sprite.png')
        self.dir_x = 0
        self.dir_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.frame = 0
        self.height = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


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


    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event((key_event))