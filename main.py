import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

my_turtle = turtle.Turtle()
my_turtle.pencolor("red")
my_turtle.pensize(3)
my_turtle.speed(1)

side_length = 150
for _ in range(4):
    my_turtle.forward(side_length)
    my_turtle.left(90)

screen.exitonclick()