import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def hand_pos():
    global handx
    global handy
    handx = random.randint(100, 1180)
    handy = random.randint(100, 924)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass

def move_character():
    global dir
    global dir2
    global x
    global y

    if x > handx and y > handy:
        dir = -1
        dir2 = -1
        incline = (y - handy) / (x - handx)
        x -= 1
        y -= incline
    elif x > handx and y < handy:
        dir = -1
        dir2 = -1
        incline = (y - handy) / (x - handx)
        x -= 1
        y -= incline
    elif x < handx and y < handy:
        dir = 1
        dir2 = 1
        incline = (y - handy) / (x - handx)
        x += 1
        y += incline
    elif x < handx and y > handy:
        dir = 1
        dir2 = 1
        incline = (y - handy) / (x - handx)
        x += 1
        y += incline

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
handx = random.randint(100, 700)
handy = random.randint(100, 600)
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0 # -1 left, +1 right
dir2 = 0 # -1 left, +1 right

while running:
    if handx == x and handy == y:
        hand_pos()

    move_character()
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(handx, handy)
    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif dir == 0 and dir2 == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dir == 0 and dir2 == - 1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()


    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()

