import turtle

def draw_square(some_turtle):
	for _ in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# Create the turtle Brad - Draw square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(6)
	for _ in range(36):
		draw_square(brad)
		brad.right(10)
	
	# Create the turtle Angie - Draw a Circle
	"""
	angie = turtle.Turtle()
	angie.color("blue")
	angie.shape("arrow")
	angie.circle(100)
	"""

	window.exitonclick()

draw_art()