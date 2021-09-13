import turtle as tur
import sys

tur.Turtle()
tur.shape("turtle")
screen = tur.getscreen()

def up():
    tur.seth(90)
    tur.forward(50)

def down():
    tur.seth(270)
    tur.forward(50)

def left():
    tur.seth(180)
    tur.forward(50)

def right():
    tur.seth(0)
    tur.forward(50)

def endProgram():
    sys.exit()

def reset():
    tur.reset()

screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(endProgram, "q")
screen.onkeypress(reset, 'Escape')

screen.listen()
screen.mainloop()