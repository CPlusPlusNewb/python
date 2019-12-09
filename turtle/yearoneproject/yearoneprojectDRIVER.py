import tkinter as tk
import turtle
import random
import need
import Prestonscode as pn
import subprocess
import socket
import getpass
import os
#p = turtle.Turtle()
#t = turtle.Turtle()
#screen = turtle.Screen()
menu_color = "#1ecbcb" #turtle.textinput("color", "input menu color (HEX):")
#staroreye = turtle.textinput("", "input menu color (HEX):")

def ipaadress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#not meh code. https://stackoverflow.com/a/25850698
	s.connect(("8.8.8.8", 80))#not meh code. https://stackoverflow.com/a/25850698
	print(s.getsockname()[0])#not meh code. https://stackoverflow.com/a/25850698
	s.close()#not meh code. https://stackoverflow.com/a/25850698

print("Please click somewhere")

#hostname = socket.gethostname()    
#ipaadress() #not meh code.
#print ("computer Host name: " + hostname)
#print ("Fully qualified name: " + socket.getfqdn(socket.gethostname()))#this was just looking at the socket module, this looked interesting
#path = os.getcwd()#didn't make this either
##print ("Computer UID (User ID): " + str(os.getuid())) #this is kind of dumb, ngl
#print ("Username: " + getpass.getuser())#found the getpass module on : https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/

#pn.menucol(menu_color)

def bruh():
	try:
		pn.menucol(menu_color)
		turtle.onscreenclick(pn.get_mouse_click_coor)
	finally:
		turtle.Terminator()
		
def bruh2():
	try:
		pn.menucol("black")
		turtle.onscreenclick(pn.get_mouse_click_coor2)
	finally:
		turtle.Terminator()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.option_add("*Font", "courier 10")
root.minsize(1000, 800)
root.title("Phrog")
	
t = tk.Button(root, text = "Do Ezekiels Code", font =("courier", "20"), command=bruh)#root, text, font, command
t.pack()

z = tk.Button(root, text = "Do Shanes Code", font =("courier", "20"), command=bruh2)#root, text, font, command
z.pack()

p = tk.Button(root, text = "Exit", font =("courier", "20"), command=exit)#root, text, font, command
p.pack()

p = tk.Label(root, text = "*** Happy Birthday Ezekiel ***", font =("courier", "10"))#root, text, font, command
p.pack()

a = tk.Label(root, text = " _   _     _       _         ___               _                        __        _    _      _                         _   __ _                                                                                        _           _   ", font =("courier", "5"), pady = 0)#root, text, font, command
b = tk.Label(root, text = "| |_| |__ (_)___  (_)___    / _ \_ __ ___  ___| |_ ___  _ __  ___      /__\______| | _(_) ___| |___      __ _ _ __   __| | / _\ |__   __ _ _ __   ___  ___   _   _  ___  __ _ _ __    ___  _ __   ___   _ __  _ __ ___ (_) ___  ___| |_ ", font =("courier", "5"), pady = 0)#root, text, font, command
c = tk.Label(root, text = "| __| '_ \| / __| | / __|  / /_)/ '__/ _ \/ __| __/ _ \| '_ \/ __|    /_\|_  / _ \ |/ / |/ _ \ / __|    / _` | '_ \ / _` | \ \| '_ \ / _` | '_ \ / _ \/ __| | | | |/ _ \/ _` | '__|  / _ \| '_ \ / _ \ | '_ \| '__/ _ \| |/ _ \/ __| __|", font =("courier", "5"), pady = 0)#root, text, font, command
d = tk.Label(root, text = "| |_| | | | \__ \ | \__ \ / ___/| | |  __/\__ \ || (_) | | | \__ \_  //__ / /  __/   <| |  __/ \__ \_  | (_| | | | | (_| | _\ \ | | | (_| | | | |  __/\__ \ | |_| |  __/ (_| | |    | (_) | | | |  __/ | |_) | | | (_) | |  __/ (__| |_ ", font =("courier", "5"), pady = 0)#root, text, font, command
e = tk.Label(root, text = " \__|_| |_|_|___/ |_|___/ \/    |_|  \___||___/\__\___/|_| |_|___( ) \__//___\___|_|\_\_|\___|_|___( )  \__,_|_| |_|\__,_| \__/_| |_|\__,_|_| |_|\___||___/  \__, |\___|\__,_|_|     \___/|_| |_|\___| | .__/|_|  \___// |\___|\___|\__|", font =("courier", "5"), pady = 0)#root, text, font, command
f = tk.Label(root, text = "                                                                 |/                                |/                                                        |___/                                     |_|           |__/               ", font =("courier", "5"), pady = 0)#root, text, font, command
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()

root.mainloop()
#if __name__ == '__main__':
	#main()
	
	#not really needed, bc i cant get it to display properly
	#canvas = screen.getcanvas()#this is just to look epic, i got it from: https://stackoverflow.com/questions/35732851/pythonturtle-module-mouse-cursor-position-in-window
	#canvas.bind('<Motion>', motion)#this is just to look epic, i got it from: https://stackoverflow.com/questions/35732851/pythonturtle-module-mouse-cursor-position-in-window
	
	#screen.cursor
	#need.triangle_filled90(100, 100, 100, 100, menu_color)
