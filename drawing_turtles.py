import turtle


#def draw_square(joe_turtle):
#    for i in range(1, 5):
#        joe_turtle.forward(100)
#        joe_turtle.right(90)


#def draw_circle(nick_turtle):
#    for i in range(1):
#        nick_turtle.circle(50)


def draw_triangle(kevin_turtle):
    for i in range(1):
        kevin_turtle.forward(100)
        kevin_turtle.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")

#    joe = turtle.Turtle()
#    joe.shape("turtle")
#    joe.color("orange")
#    joe.speed(0)

#    for i in range(1, 37):
#        draw_square(joe)
#        joe.right(10)

#    nick = turtle.Turtle()
#    nick.shape("turtle")
#    nick.color("purple")
#    nick.speed(0)

#    for i in range(1, 37):
#        draw_circle(nick)
#        nick.right(10)

    kevin = turtle.Turtle()
    kevin.shape("turtle")
    kevin.color("red")
    kevin.speed(2)

    for i in range(1, 37):
        draw_triangle(kevin)
        kevin.right(10)

    window.exitonclick()


draw_art()

# shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
# speed: fastest: 0, fast: 10, normal: 6, slow: 3, slowest: 1
