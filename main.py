import pandas  # import pandas module
import turtle  # import turtle module

data = pandas.read_csv("regionebi.csv")  # read data from csv file
region_list = data.regionebi.tolist()  # add regionebi from data to new list


screen = turtle.Screen()  # create screen object from Screen() class
# set up the screen
screen.title("Georgian Regions")
screen.setup(width=600, height=400)

image = "Georgia.svg.gif"

turtle.addshape(image)  # create new shape for the turtle, witch will be Georgian map.gif
turtle.shape(image)  # use that shape to display our map

guessed_regions = []

while len(guessed_regions) < 13:  # game will run before all 13 regions are guessed
	user_guess = screen.textinput(title=F"{len(guessed_regions)}/13", prompt="Write the name of a region").title()  # ask
	# user for an input, and convert it to titlecase
	if user_guess == "Exit":
		break  # to end the loop manually
	for region in region_list:
		if user_guess == region:  # compare users answer to actual region
			check_region = data[data.regionebi == region]  # get hold of the region in data
			new_turtle = turtle.Turtle()  # create new turtle
			new_turtle.penup()
			new_turtle.hideturtle()
			new_turtle.goto(int(check_region.x), int(check_region.y))  # go on that regions x and y coordinates
			new_turtle.write(f"{region}")  # write name of the region
			guessed_regions.append(region)  # append tu the guessed regions list


