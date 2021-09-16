import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 402
y = 90
dir = 0
count = 1
degree = 270

while(1):
    if(count % 2 == 0):
        if(dir == 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x + 2
            if(x >= 800):
                dir = 1
            if(x == 400):
                count = 1
        elif(dir == 1):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 2
            if(y >= 600):
                dir = 2
        elif(dir == 2):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 2
            if(x <= 0):
                dir = 3
        else:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 2
            if(y <= 90):
                dir = 0
        delay(0.01)
    else:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        degree = degree + 2
        if(degree==360):
            degree = 0
        if(degree == 270):
            count = 0
        x = 225*math.cos(degree / 360 * 2 * math.pi) + 400
        y = 225*math.sin(degree / 360 * 2 * math.pi) + 300
        delay(0.01)

close_canvas()
