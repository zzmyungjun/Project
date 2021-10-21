import game_framework
import title_state
from pico2d import *

name = "Dungeon"
boy = None
background = None
x, y, frame, height, dirx, diry = 400,300,0,0,0,0


class Background:
    def __init__(self):
        self.image = load_image('던전5(600).png')
    def draw(self):
        self.image.draw(400,300)

class Boy:
    global x, y, frame, height, dirx, diry

    def __init__(self):
        self.x,self.y = 400,300
        self.frame =0
        self.image = load_image('character_sprite.png')
        self.dir = 0



    def draw(self):
        self.image.clip_draw(frame * 40, height * 52, 40, 52, x, y)


def enter():
    global background,boy
    boy = Boy()
    background = Background()

def exit():
    global background,boy
    del(background)
    del(boy)

def pause():
    pass

def resume():
    pass

def handle_events():
    global x,y,height,frame,dirx,diry

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            frame = (frame + 1) % 4
            height = 2
            dirx -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            frame = (frame + 1) % 4
            height = 0
            dirx += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            frame = (frame + 1) % 4
            height = 1
            diry += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            frame = (frame + 1) % 4
            height = 3
            diry -= 1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            frame = 0
            dirx = 0
            diry = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            frame = 0
            dirx = 0
            diry = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_UP:
            frame = 0
            dirx = 0
            diry = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_DOWN:
            frame = 0
            dirx = 0
            diry = 0
def update():
    pass
    # boy.update()


def draw():
    global x,y,dirx,diry,frame
    clear_canvas()
    background.draw()
    boy.draw()

    update_canvas()


    x+=dirx * 3
    y+=diry * 3

    delay(0.01)

