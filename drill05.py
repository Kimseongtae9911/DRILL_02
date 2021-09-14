import turtle

turtle.shape("turtle")


def up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()


turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(reset, 'Escape')

turtle.listen()

