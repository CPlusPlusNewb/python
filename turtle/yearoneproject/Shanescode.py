import turtle
import need

def star(x, y, length):
	try:
		turtle.tracer(0, 0)
		need.penupsetxy(x - length / 2, y)
		for side in range (0,5):
			if (side == 1):
				turtle.color("red")
			elif (side == 2):
				turtle.color("green")
			elif (side == 3):
				turtle.color("blue")
			elif (side == 4):
				turtle.color("red")
			elif (side == 5):
				turtle.color("green")
			turtle.forward(length)
			turtle.right(144)
		turtle.update()
	finally:
		turtle.Terminator()
