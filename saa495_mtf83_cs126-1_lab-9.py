# Scott Ames / Matthew Flanders
# saa495 / mtf83
# Section 01
# Lab 9: Draw Stars

import turtle


def read_coords(file):
    # tuple to hold seperate star dictionaries
    coordinates_dict = {}
    magnitudedict = {}
    star_name_dict = {}

    # opening the file and reading the lines
    inputfile = open(file, "r")
    lines = inputfile.readlines()

    # organize files into appropriate dictionaries
    for line in lines:
        splitline = line.split(" ")
        xy = (splitline[0], splitline[1])
        HDN = splitline[3]
        magnitude = splitline[4]
        HRN = splitline[5]
 
       # replace \n
        if "\n" in HRN:
            HRN.replace("\n", "")

        if len(splitline) > 6:
            starname = splitline[6:]
            starname = str(starname)

        coordinates_dict[HDN] = (xy)
        magnitudedict[HDN] = (magnitude)

    return (coordinates_dict, magnitudedict)


def plot_plain_stars(picture_size, coordinates_dict):
    # step 0: setup turtle (background color, fill color, etc)
    turtle.fillcolor("white")
    turtle.bgcolor("black")
    turtle.setup(picture_size, picture_size)

    # Step 1: Loop through the keys in the dictionary (HDN #'s) and
    # get the x, y coords for that star by the HDN and
    # Scale them to your picture
    for star_HDN in coordinates_dict.keys():
        coordinates = coordinates_dict[star_HDN]
        # Ex: (x, y)
        xCoord = float(coordinates[0] * (picture_size / 2))
        yCoord = float(coordinates[1] * (picture_size / 2))
        # Step 3: Pen up, go to those coords
        turtle.pu()
        turtle.goto(xCoord, yCoord)
        # Step 4: Pen down, draw a square / fill square
        turtle.pd()
        for i in range(4):
            turtle.forward(2)
            turtle.right(90)

        turtle.exitonclick()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudedict):
    # setup turtle (background color, fill color, etc)
    turtle.fillcolor("white")
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.setup(picture_size, picture_size)
    turtle.speed(0)
    turtle.tracer(8, 25)

    # Loop through the keys in the dictionary (HDN #'s) and
    # get the x, y coords for that star by the HDN and
    # Scale them to your picture
    for star_HDN in coordinates_dict.keys():
        coordinates = coordinates_dict[star_HDN]
        # Ex: (x, y)
        xCoord = float(coordinates[0]) * (float(picture_size) / 2)
        yCoord = float(coordinates[1]) * (float(picture_size) / 2)
        star_magnitude = magnitudedict[star_HDN]
        star_magnitude = round(10.0 / (float(star_magnitude) + 2))

        # set max magnitude
        if star_magnitude > 8:
            star_magnitude = 8

        # Pen up, go to those coords
        turtle.pu()
        turtle.goto(xCoord, yCoord)

        # Pen down, draw a square / fill square
        turtle.pd()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(star_magnitude)
            turtle.right(90)
        turtle.end_fill()

    turtle.exitonclick()


def main():
    stars_tuple = read_coords("stars.txt")
    plot_by_magnitude(500, stars_tuple[0], stars_tuple[1])


if __name__ == "__main__":
    main()
