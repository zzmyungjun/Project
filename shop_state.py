import game_framework
import game_world
import main_state
import server

from Swords import *
from pico2d import *
from Shop import *

name = "shop_state"

def enter():
    server.shop = Shop()
    server.background = Background()
    server.sword_1 = Sword_1()
    server.sword_2 = Sword_2()
    game_world.add_object(server.background, 0)
    game_world.add_object(server.shop, 1)
    game_world.add_object(server.sword_1, 1)
    game_world.add_object(server.sword_2, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(main_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, event.y
            if x >= server.sword_1.x - 21 and x <= server.sword_1.x + 19:
                if y >= server.sword_1.y - 19 and y <= server.sword_1.y + 21:
                    game_world.remove_object(server.sword_1)

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()