import game_framework
import loading_state
import bossroom1_state
import main_state
import game_world
import server
import collision
from pico2d import *

from dungeon_portal import Portal
from bossroom import Bossroom_1
from boss import Boss1
from at_stone import Stone
from slime import Slime
from boy import *
from boss_hand import Hand

name = "bossroom1_state"


def enter():
    server.boy = Boy()
    server.bossroom1 = Bossroom_1()
    server.boss1 = Boss1()
    # server.slimes = [Slime() for i in range(6)]
    server.portal = Portal()

    game_world.add_object(server.bossroom1, 0)
    # game_world.add_objects(server.slimes, 1)
    game_world.add_object(server.boss1, 1)
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
    # for slime in server.slimes:
    #     if collision.collide(server.boy, slime):
    #         slime.idle_height = 4 * 27
    #         server.boy.hp -= 1
    #         if server.boy.cur_state == AttackState:
    #             slime.hp -= 10
    #             if slime.hp <= 0:
    #                 server.slimes.remove(slime)
    #                 game_world.remove_object(slime)
    if server.boss1.height >= 2 and server.boss1.height < 3:
        server.stone = Stone()
        game_world.add_object(server.stone, 1)
        if server.stone.count == 0:
            server.stone.shotgun()
            server.stone.count = 1
        if collision.collide(server.boy, server.stone):
            server.boy.hp -= 3

    if server.boss1.height >= 3 and server.boss1.height < 3.5:
        server.hand = Hand()
        game_world.add_object(server.hand, 1)
        delay(0.01)
        if collision.collide(server.boy, server.hand):
            server.boy.hp -= 100

    if collision.collide(server.boss1,server.boy):
        server.boy.hp -= 1.5
        if server.boy.cur_state == AttackState:
            server.boss1.hp -= 2
            if server.boss1.hp <= 0:
                game_framework.change_state(loading_state)


    # if len(server.slimes) == 0:
    #     delay(1)
    #     game_framework.change_state(bossroom1_state)

    # if server.boy.hp <= 0:
    #     game_framework.change_state(loading_state)
    # if collision.collide(server.portal, server.boy):
    #     game_framework.change_state(loading_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()