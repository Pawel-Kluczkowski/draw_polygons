import turtle
from dataclasses import dataclass


@dataclass
class UserInput:
    sides: int
    size: int
    coord_x: int
    coord_y: int


wn = turtle.Screen()
plotter = turtle.Turtle()
wn.screensize(1920, 1080)
wn.title(wn.screensize())


def get_user_input() -> UserInput:
    sides = int(turtle.numinput("Polygon sides", "Enter number of polygon sides", 3, minval=3, maxval=100))
    size = int(turtle.numinput("Polygon size", "Enter size of a side", 30, minval=10, maxval=100))
    coord_x = int(turtle.numinput("Coord X", "Enter value of coord x", 30, minval=0, maxval=1920))
    coord_y = int(turtle.numinput("Coord Y", "Enter size of a coord y", 30, minval=0, maxval=1080))
    user_input = UserInput(sides=sides, size=size, coord_x=coord_x, coord_y=coord_y)
    return user_input


def initialize_plotter(user_input: UserInput):
    plotter.pu()
    plotter.goto(user_input.coord_x, user_input.coord_y)
    plotter.pd()


def draw_polygon(user_input: UserInput):
    for s in range(user_input.sides):
        plotter.forward(user_input.size)
        plotter.right(180 - (((user_input.sides - 2) * 180) / user_input.sides))


def main():
    user_input = get_user_input()
    initialize_plotter(user_input=user_input)
    draw_polygon(user_input=user_input)

    while True:
        response = turtle.textinput("Do you want to draw another polygon?", " Type 'yes'  or 'y' or 'no' or 'n' ")
        if response == "yes" or response == "y":
            main()
        elif response == "no" or response == "n":
            break
        else:
            continue

    wn.mainloop()


main()
