import game_framework
import loading_state
import main_state
import game_world
import server
import collision
from pico2d import *

from dungeon_portal import Portal
from dungeon import Dungeon
from slime import Slime
from boy import *


name = "dungeon_state"


def enter():
    server.boy = Boy()
    server.dungeon = Dungeon()
    server.slimes = [Slime() for i in range(6)]
    server.portal = Portal()
    game_world.add_object(server.dungeon, 0)
    game_world.add_objects(server.slimes, 1)
    game_world.add_object(server.boy, 1)
    game_world.add_object(server.portal, 1)

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
    for slime in server.slimes:
        if collision.collide(server.boy, slime):
            slime.idle_height = 4 * 27
            server.boy.hp -= 1
            if server.boy.cur_state == AttackState:
                slime.hp -= 10
                if slime.hp <= 0:
                    server.slimes.remove(slime)
                    game_world.remove_object(slime)

    if len(server.slimes) == 0:
        server.count = 1
        game_framework.change_state(loading_state)

    if server.boy.hp <= 0:
        game_framework.change_state(loading_state)
    if collision.collide(server.portal, server.boy):
        game_framework.change_state(loading_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()