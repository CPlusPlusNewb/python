import tkinter as tk
import turtle
import random
import need
import Ezekielscode as ec
import Shanescode as sm
menu_color = ""

def menucol(col):
	try:
		global menu_color
		menu_color = col
	finally:
		turtle.Terminator()

def get_mouse_click_coor(x, y):#this is da main
	try:
		mouseposx = x
		mouseposy = y
		cordprint = (str(x) + ", " + str(y))
		print('"eye" at: '+ cordprint)#debug
		turtle.hideturtle()
		#need.rectangle_filled(x, y, random.randint(10,100), random.randint(10,100), menu_color)
		ec.eye(x, y, random.randint(0, 2), random.randint(100, 120), random.randint(50, 100),random.randint(10, 50))
		#sm.star(x, y, random.randint(20, 50), menu_color)
		print(str(menu_color))
		need.text(x, y, cordprint, "#000000", 8, "")#debug 
		turtle.penup()
	finally:
		turtle.Terminator()
def get_mouse_click_coor2(x, y):#this is da main
	try:
		mouseposx = x
		mouseposy = y
		cordprint = (str(x) + ", " + str(y))
		print('"eye" at: '+ cordprint)#debug
		turtle.hideturtle()
		#need.rectangle_filled(x, y, random.randint(10,100), random.randint(10,100), menu_color)
		#ec.eye(x, y, random.randint(0, 2), random.randint(100, 120), random.randint(50, 100),random.randint(10, 50), menu_color)
		sm.star(x, y, random.randint(20, 50))
		print(str(menu_color))
		need.text(x, y, cordprint, menu_color, 8, "")#debug 
		turtle.penup()
	finally:
		turtle.Terminator()
