import turtle

turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.pensize(5)
turtle.penup()
turtle.forward(90)
turtle.left(90)
turtle.forward(55)
turtle.pendown()
turtle.home()

turtle.left(60)
turtle.forward(173)
turtle.left(180)
turtle.home()

turtle.left(90)
turtle.forward(200)
turtle.left(180)
turtle.home()
turtle.left(180)

turtle.right(60)
turtle.forward(173)
turtle.left(180)
turtle.home()

turtle.left(180)
turtle.penup()
turtle.forward(90)
turtle.right(90)
turtle.forward(55)
turtle.pendown()
turtle.home()

turtle.circle(100)

turtle.right(90)
turtle.forward(30)

turtle.penup()
turtle.right(90)
turtle.forward(30)
turtle.pendown()

turtle.left(90)
turtle.fillcolor('brown')
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
turtle.end_fill()

for i in range(2):
    turtle.left(90)
    turtle.forward(30)

turtle.left(90)
turtle.penup()
turtle.forward(90)
turtle.right(90)
turtle.forward(55)
turtle.pendown()
turtle.goto(-30,-30)

turtle.right(90)
turtle.forward(60)
turtle.goto(90,55)

turtle.exitonclick()