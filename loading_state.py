import game_framework
import dungeon_state
import main_state
from pico2d import *


name = "loading_state"
animation = None
a = 0
b = 0

def enter():
    global animation
    animation = load_image('bubble_sprite.png')



def exit():
    global animation
    del(animation)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(dungeon_state)


def draw():
    global a,b
    clear_canvas()
    animation.clip_draw(1024 * a, 768 * b, 1024, 768, 512, 383)
    update_canvas()
    delay(0.1)
    a = (a + 1) % 4
    b = (b + 1) % 4




def update():
    pass


def pause():
    pass


def resume():
    pass





