import tkinter as tk
import turtle
import Prestonscode as pn
menu_color = "#1ecbcb" #turtle.textinput("color", "input menu color (HEX):")
def bruh():
	pn.menucol(menu_color)
	turtle.onscreenclick(pn.get_mouse_click_coor)
	
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.minsize(800, 800)
root.option_add("*Font", "courier 10")
pn.menucol(menu_color)
button = tk.Button(frame, text="QUIT", fg="red", font =("courier", "20"), command=quit)
button.pack()#(side=tk.LEFT)
slogan = tk.Button(frame, text="Do Ezekiels Code", font =("courier", "20"), command=pn.main())
slogan.pack()#(side=tk.LEFT)

root.mainloop()
