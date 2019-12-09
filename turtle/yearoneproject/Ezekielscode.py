import turtle
def eye(x, y, penwidth, first, second, third):
	try:
		yeet = turtle.Turtle()
		turtle.tracer(0, 0)
		for i in range(45):
			#yeet.pencolor("red")
			yeet.penup()
			#if (yeet.pensize() != 5)
			yeet.pensize(5)
			yeet.goto(x, y)
			yeet.pendown()
			yeet.pencolor("red")
			yeet.width(penwidth)
			yeet.forward(first)#200
			yeet.pencolor("green")
			yeet.left(100)
			yeet.forward(second)#160
			yeet.pencolor("blue")
			yeet.right(80)
			yeet.forward(third)#30
			yeet.right(70)
			yeet.penup()
		turtle.update()
		#yeet.pensize(1)
	finally:
		turtle.Terminator()
