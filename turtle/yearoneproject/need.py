import tkinter as tk
import turtle
#pn code
import math 
#turtle.tracer(0, 0)
def penupsetxy(xcord, ycord):
	turtle.penup()
	turtle.setx(xcord)
	turtle.sety(ycord)
	turtle.pendown()

def rectangle_outline(x, y, width, height, color):#this is really poop, but its the first thing i made so of-course it is dumby
	turtle.color(color)
	penupsetxy(x, y)
	for _ in range(2):#not my code, but is nice
		turtle.forward(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.right(90)
	turtle.penup()
	
def rectangle_filled(x, y, width, height, color):
	turtle.fillcolor(color)
	penupsetxy(x, y)
	turtle.begin_fill()
	for _ in range(2):#not my code, but is nice
		turtle.forward(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.right(90)
	turtle.end_fill()
	turtle.penup()
	
def triangle_outlined_90(x, y, num, num2, color):
	bruh = math.sqrt(num**2 + num**2)
	print(bruh)
	turtle.color(color)
	penupsetxy(x, y)
	turtle.right(180)
	turtle.forward(num)
	turtle.right(90)
	turtle.forward(num2)
	turtle.right(135)
	turtle.forward(bruh)
	turtle.penup()
	turtle.right(180 - 135)
	turtle.penup()
	
def triangle_filled90(x, y, num, num2, color):
	bruh = math.sqrt(num**2 + num**2)
	print(bruh)
	turtle.fillcolor(color)
	penupsetxy(x, y)
	turtle.begin_fill()
	turtle.right(180)
	turtle.forward(num)
	turtle.right(90)
	turtle.forward(num2)
	turtle.right(135)
	turtle.forward(bruh)
	turtle.right(180 - 135)
	turtle.end_fill()
	turtle.penup()

def line_wide(x, y, width, color):
	turtle.color(color)
	penupsetxy(x, y)
	turtle.forward(width)
	turtle.penup()
	
def line_long(x, y, height, color):
	turtle.color(color)
	penupsetxy(x, y)
	turtle.right(90)
	turtle.forward(height)
	turtle.left(90)
	turtle.penup()
	
def text(x, y, inputtxt, color, font_size, style):
	style = ('Verdana', font_size, style)
	turtle.color(color)
	penupsetxy(x, y)
	turtle.write(inputtxt, font=style)
	turtle.penup()
#turtle.update()
