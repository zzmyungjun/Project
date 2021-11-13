import game_framework
import title_state
import game_world
from pico2d import *

from village import Village
from boy import Boy


name = "main_state"
boy = None
village = None

# class Boy:
#     global x, y, frame, height, dirx, diry
#
#     def __init__(self):
#         self.x,self.y = 400,300
#         self.frame =0
#         self.image = load_image('character_sprite.png')
#         self.dir = 0
#
#
#
#     def draw(self):
#         self.image.clip_draw(frame * 40, height * 52, 40, 52, x, y)


def enter():
    global village,boy
    boy = Boy()
    village = Village()
    game_world.add_object(village, 0)
    game_world.add_object(boy, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    # global x,y,height,frame,dirx,diry
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit(title_state)
        else:
            boy.handle_event(event)

def update():
    boy.update()


def draw():
    # global x,y,dirx,diry,frame
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()