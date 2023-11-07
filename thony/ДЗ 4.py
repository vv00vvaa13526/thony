import turtle

width = turtle.window_width()
height = turtle.window_height()

turtle.speed(1)

turtle.goto(width,-height)

turtle.forward(-50)

turtle.goto(width,height)

turtle.goto(-width,-height)

turtle.forward(50)

turtle.goto(-width,height)

turtle.home()

turtle.exitonclick()