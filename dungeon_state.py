import game_framework
import loading_state
import main_state
import game_world
from pico2d import *

from village_portal import Portal
from dungeon import Dungeon
from slime import Slime
from boy import *


name = "dungeon_state"
boy = None
dungeon = None
portal = None
slimes = []

def enter():
    global dungeon, boy, slimes, portal
    boy = Boy()
    dungeon = Dungeon()
    slimes = [Slime() for i in range(10)]
    portal = Portal()

    game_world.add_object(dungeon, 0)
    game_world.add_objects(slimes, 1)
    game_world.add_object(boy, 1)
    game_world.add_object(portal, 1)

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
            boy.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for slime in slimes:
        if collide(boy, slime):
            slime.idle_height = 4 * 27
            boy.hp -= 1
            if boy.cur_state == AttackState:
                slime.hp -= 10
                if slime.hp <= 0:
                    slimes.remove(slime)
                    game_world.remove_object(slime)

    if boy.hp <= 0:
        game_framework.change_state(loading_state)
    if collide(portal, boy):
        game_framework.change_state(loading_state)


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