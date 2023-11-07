import turtle

width = turtle.window_width()
height = turtle.window_height()

turtle.speed(1)
turtle.goto(width,-height)

turtle.speed(2)
turtle.goto(width,height)

turtle.speed(4)
turtle.goto(-width,-height)

turtle.speed(8)
turtle.goto(-width,height)




turtle.exitonclick()
