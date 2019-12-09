import tkinter as tk
import turtle
import need
#pn code
import colors as color
import math 
turtle.tracer(0, 0)
mouseposx = 0
mouseposy = 0
menu_color = "#1ecbcb"

def get_mouse_click_coordianates(x, y):
	global mouseposx
	mouseposx = x
	global mouseposy
	mouseposy = y

turtle.onscreenclick(get_mouse_click_coordianates)

def menucolor(color):
	menu_color = color
	
def checkbox(x, y, name, colenabled, coldisabled, mouseposxcord, mouseposycord):
	mouseposxcord = x + 10
	mouseposycord = y - 10
	print("new thing = " + str(mouseposxcord) + ", " + str(mouseposycord))
	need.rectangle_outline(x, y, 10, 10, "#000000")
	if (x + 10 >= mouseposxcord >= x):
		if (y - 10 >= mouseposycord >= y):
			need.rectangle_filled(x + 1, y - 1, 8, 8, colenabled)
			print("filled = yes")
	else:
		need.rectangle_filled(x + 1, y - 1, 8, 8, coldisabled)
turtle.update()
