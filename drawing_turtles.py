import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    tim = turtle.Turtle()
    tim.shape("turtle")
    tim.color("orange")
    tim.speed(1)

    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)

    nick = turtle.Turtle()
    nick.shape("turtle")
    nick.color("purple")

    nick.circle(100)

    window.exitonclick()


draw_square()

# shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
# speed: fastest: 0, fast: 10, normal: 6, slow: 3, slowest: 1
