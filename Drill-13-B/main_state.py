import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

import server

name = "MainState"

def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)

    server.bricks = [Brick(300+300*i, 100+50*i) for i in range(5)]
    game_world.add_objects(server.bricks, 1)



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


    # for brick in bricks:
    #     if collide(boy, brick):
    #         tleft, tbottom, tright, ttop = brick.get_bb()
    #         bleft, bbottom, bright, btop = boy.get_bb()
    #         brick_speed = brick.get_speed()
    #         boy.y = ttop + 30
    #         boy.x += brick_speed * game_framework.frame_time
    #         print(boy.x)
    #         print(tright)
    #         if bright >= tright:
    #             boy.x = tright - 30
    #         elif bleft <= tleft:
    #             boy.x = tleft + 30

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






