import turtle

BACKGROUND_Color = "#9EC388"
CRUST_Color = "#ECA84F"
SAUCE_Color = "#AD0509"
CHEESE_Color = "#FBC70F"

PEPPERONI_Location = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_Color)
screen.title("My Pizza")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

draw_circle(150, CRUST_Color, CRUST_Color)
move_turtle(0, 25)
draw_circle(125, SAUCE_Color, CHEESE_Color)

for location in PEPPERONI_Location:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_Color, SAUCE_Color)
