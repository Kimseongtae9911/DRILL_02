import turtle
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

count = 6
height = -100
while(count > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-200, height)
    turtle.pendown()
    height += 100
    count -= 1

turtle.right(90)
turtle.penup()
turtle.goto(-200, 300)
turtle.pendown()
width = -100
count = 6
while(count > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(width, 300)
    turtle.pendown()
    width += 100
    count -= 1
   
    
