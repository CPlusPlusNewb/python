#this is from my csgo look alike cheat menu in turtle i worked on
def penupsetxy(xcord, ycord, daturtle):
	daturtle.penup()
	daturtle.setx(xcord)
	daturtle.sety(ycord)
	daturtle.pendown()

def text(x, y, inputtxt, color, font_size, style, font, alignment, daturtle):
	style = (font, font_size, style)
	daturtle.color(color)
	penupsetxy(x, y, daturtle)
	daturtle.write(inputtxt, align=alignment, font=style)
	daturtle.penup()

def line_wide(x, y, width, color, daturtle):
	daturtle.color(color)
	penupsetxy(x, y, daturtle)
	daturtle.forward(width)
	daturtle.penup()
	
def line_long(x, y, height, color, rotation, daturtle):
	daturtle.color(color)
	penupsetxy(x, y, daturtle)
	daturtle.right(rotation)
	daturtle.forward(height)
	daturtle.left(-rotation)
	daturtle.penup()
