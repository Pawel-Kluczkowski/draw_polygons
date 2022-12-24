import turtle


def draw_polygon():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    wn.screensize(1920, 1080)
    wn.title(wn.screensize())
    sides = int(turtle.numinput("Polygon sides", "Enter number of polygon sides", 3, minval=3, maxval=100))
    size = turtle.numinput("Polygon size", "Enter size of a side", 30, minval=10, maxval=100)
    coord_x = turtle.numinput("Coord X", "Enter value of coord x", 30, minval=0, maxval=1920)
    coord_y = turtle.numinput("Coord Y", "Enter size of a coord y", 30, minval=0, maxval=1080)
    alex.pu()
    alex.goto(coord_x, coord_y)
    alex.pd()
    # def f(x,y):
    # alex.goto(x,y)
    # while True:
    # alex.onclick(f)

    for s in range(sides):
        alex.forward(size)
        alex.right(180 - (((sides - 2) * 180) / sides))

    while True:
        response = turtle.textinput("Do you want to draw another polygon?", " Type 'yes'  or 'y' or 'no' or 'n' ")
        if response == "yes" or response == "y":
            draw_polygon()
        elif response == "no" or response == "n":
            break
        else:
            continue

    wn.mainloop()


draw_polygon()
