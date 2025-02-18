import turtle

screen = turtle.Screen()
screen.bgcolor("white")

star = turtle.Turtle()
star.shape("turtle")
star.color("black")
star.speed(1)


def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)
draw_star(star, 200)


star.hideturtle()
turtle.done()
