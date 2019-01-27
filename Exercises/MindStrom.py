import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor('yellow')

    brad = turtle.Turtle()
    brad.speed(1)

    moves = 0
    while moves < 4:
        brad.forward(100)
        brad.right(90)
        moves = moves + 1

    window.exitonclick()


draw_square()
