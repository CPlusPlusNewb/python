import tkinter as tk
import turtle
import random
import need
import colors as color
#==========================
rage = 0
legit = 0
visuals = 0
misc = 0
config = 0
#==========================#setup
_width = 600
_height = 450
posx = -300
posy = 250
turtle.bgcolor("#ff9933")
turtle.speed(50)
screen = turtle.Screen()
#==========================#checkbox
def checkbox(x, y, name, col, mouseposxcordcb, mouseposycordcb):
	mouseposxcordcb = x + 10
	mouseposycordcb = y - 10
	print("new thing = " + str(mouseposxcordcb) + ", " + str(mouseposycordcb))
	need.rectangle_outline(x, y, 10, 10, "#000000")
	need.rectangle_filled(x + 1, y - 1, 8, 8, col)
#==========================#colorsfortabs
#menu_color = turtle.textinput("color", "input menu color:")
menu_color = "#1ecbcb"
legitbot_color = "#999999"
ragebot_color = "#999999"
visals_color = "#999999"
misc_color = "#999999"
config_color = "#999999"
#==========================
newheight = _height - 10
newwidth = _width - 10
newx = posx  + 5
newy = posy - 5
#==========================tabxy
newxtab = newx  + 18
newytab = newy - 67
#need.rectangle_outline(newx + 12, newy - 61, newwidth - 24, newheight - 73, lighter_gray)
#need.rectangle_filled(newx + 12, newy - 61, newwidth - 24, newheight - 73, darkish_gray)
#==========================legittab
def legitbottab():
	print("Legitbottab")
#==========================vistab
def vistab():
	print("Visualstab")
#==========================misctab
def misctab():
	print("MiscTab")
#==========================cfgtab
def cfgtab():
	print("Configtab")
#==========================
bruh = 0
mouseposx = 0
mouseposY = 0
#==========================
def get_mouse_click_coor(x, y):
	global mouseposx
	mouseposx = x
	global mouseposy
	mouseposy = y
    
	global rage
	global legit
	global visuals
	global misc
	global config
    
	print("newx = " + str(newx))#debug 
	print("newy = " + str(newy))#debug 
	print(str(x) + " , " + str(y))#debug 
	turtle.hideturtle()#debug 
	turtle.tracer(0, 0)
	if ( 218 >= mouseposy >= 201):
		#if (249 >= mouseposx >= -255):
		#	bruh = 1
		#	print(bruh)
		#else:
		#	bruh = 0
		#	print(bruh)
		if (-185 >= mouseposx >= -255):
			#print("legitbot_color = true")
			need.text(newx + 40, newy - 43, "Legitbot", menu_color, 11, "")
			legitbottab()
			legit = 1
		else:
			legit = 0
			need.text(newx + 40, newy - 43, "Legitbot", color.white, 11, "")
		if (-77 >= mouseposx >= -143):
			#print("ragebot_color = true")
			need.text(newx + 150, newy - 43, "Ragebot", menu_color, 11, "")
			rage = 1
			#if (x + 10 >= mouseposx >= x):
			#	if (y - 10 >= mouseposy >= y):
			#		checkbox(newxtab, newytab, "Bruh", menu_color, mouseposx, mouseposy)
			#else:
				#checkbox(newxtab, newytab, "Bruh", color.light_gray, mouseposx, mouseposy)
		else:
			need.text(newx + 150, newy - 43, "Ragebot", color.white, 11, "")
			#checkbox(newxtab, newytab, "Bruh", color.light_gray, mouseposx, mouseposy)
			rage = 0
		if (20 >= mouseposx >= -36):
			#print("visals_color = true")
			need.text(newx + 257, newy - 43, "Visuals", menu_color, 11, "")
			vistab()
			visuals = 1
		else:
			visuals = 0
			need.text(newx + 257, newy - 43, "Visuals", color.white, 11, "")
		if (167 >= mouseposx >= 52):
			#print("misc_color = true")
			need.text(newx + 347, newy - 43, "Miscellaneous", menu_color, 11, "")
			misctab()
			misc = 1
		else:
			misc = 0
			need.text(newx + 347, newy - 43, "Miscellaneous", color.white, 11, "")
		if (249 >= mouseposx >= 199):
			#print("config_color = true")
			need.text(newx + 492, newy - 43, "Config", menu_color, 11, "")
			cfgtab()
			config = 1
		else:
			config = 0

			need.text(newx + 492, newy - 43, "Config", color.white, 11, "")
	turtle.showturtle()#debug 
	turtle.update()
def main():
	turtle.speed(0)#fastest
	turtle.hideturtle()
	need.rectangle_outline(posx, posy, _width, _height, color.black)
	need.rectangle_outline(posx + 1, posy - 1, _width - 2, _height - 2, color.light_gray)
	need.rectangle_outline(posx + 2, posy - 2, _width - 4, _height - 4, color.dark_gray)
	need.rectangle_outline(posx + 3, posy - 3, _width - 6, _height - 6, color.dark_gray)
	need.rectangle_outline(posx + 4, posy - 4, _width - 8, _height - 8, color.light_gray)
	need.rectangle_outline(posx + 5, posy - 5, _width - 10, _height - 10, color.darker_gray)
	#turtle.showturtle()#debug 
	#new things so i dont have to keep minusing by b1g numbers

	need.rectangle_filled(newx, newy, newwidth, newheight, color.darker_gray)
	need.line_wide(newx + 2, newy - 2, newwidth - 4, menu_color)#colorline
	
	need.rectangle_outline(newx + 12, newy - 16, newwidth - 24, 35, color.lighter_gray)
	need.rectangle_filled(newx + 12, newy - 16, newwidth - 24, 35, color.darkish_gray)
	
#these are here becuase they way its setup, it may look weird, but its ight
	if (bruh == 0):
		need.text(newx + 40, newy - 43, "Legitbot", color.white, 11, "")
		need.text(newx + 150, newy - 43, "Ragebot", color.white, 11, "")
		need.text(newx + 257, newy - 43, "Visuals", color.white, 11, "")
		need.text(newx + 347, newy - 43, "Miscellaneous", color.white, 11, "")
		need.text(newx + 492, newy - 43, "Config", color.white, 11, "")
	
#now we draw the body for the checkboxes on the menu, and combos, etc
	need.rectangle_outline(newx + 12, newy - 61, newwidth - 24, newheight - 73, color.lighter_gray)
	need.rectangle_filled(newx + 12, newy - 61, newwidth - 24, newheight - 73, color.darkish_gray)
	turtle.showturtle()#debug 
	#menu.menucolor(menu_color)


if __name__ == '__main__':
	main()

#turtle.onscreenclick(ragebottab)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
