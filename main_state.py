import game_framework
import loading_state
import shop_state
import game_world
import server
from pico2d import *

from village import Village
from boy import Boy
from Npc1 import Npc1
from House import House
from dungeon_portal import Portal

name = "main_state"


def enter():

    server.house = House()
    server.boy = Boy()
    server.village = Village()
    server.portal = Portal()
    server.npc1 = Npc1()
    game_world.add_object(server.village, 0)
    game_world.add_object(server.house, 1)
    game_world.add_object(server.portal, 1)
    game_world.add_object(server.npc1, 1)
    game_world.add_object(server.boy, 1)


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
            game_framework.quit()
        else:
            server.boy.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(server.portal, server.boy):
        game_framework.change_state(loading_state)
    if collide(server.npc1, server.boy):
        game_framework.change_state(shop_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True