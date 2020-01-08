'''
Test this.
https://tritech-testsite.smapply.io/

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''

import specialstuff
import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ffffed"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"
def grid(t):
    x = 0; y = 0
    while (x < 400):
	    t.penup()
	    t.goto(x,y)
	    t.pendown()
	    t.goto(x,y+400)
	    x = x + 50
    x = 0; y = 0
    while (y < 400):
	    t.penup()
	    t.goto(x,y)
	    t.pendown()
	    t.goto(x+400,y)
	    y = y + 50
    specialstuff.line_wide(0, 400, 400, '#000000', t)
    specialstuff.line_long(400, 0, 400, '#000000', 270, t)
    specialstuff.text(-165, 410, 'Circle Circumference and Diameter Plot', '#00ff00', 25, 'Verdana', 'underline bold', 'left', t)
    specialstuff.text(-45, 10, 'C\ni\nr\nc\nu\nm\nf\ne\nr\ne\nn\nc\ne', '#00ff00', 18, 'Verdana', 'bold', 'left', t)
    specialstuff.text(200, -40, 'D i a m e t e r', '#00ff00', 18, 'Verdana', 'bold', 'center', t)
    t.hideturtle()
    t.penup()

def plotCircles(t):
	d =  [3.2, 3.5, 3.4, 6.7] 
	c =  [9.6, 11, 11.1, 21.5] 
    #this is inacurate, i have 2 points where the circumference is smaller, but the diameter is bigger
	#dsorted = sorted (d, key = float)
	#csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()
	t.dot(3, red)
	t.goto(d[0] * 2,c[0]* 2)
	t.dot(3, red)
	t.goto(d[1]* 2,c[1]* 2)
	t.dot(3, red)
	t.goto(d[2]* 2,c[2]* 2)
	t.dot(3, red)
	t.goto(d[3]* 2,c[3]* 2)
	t.dot(3, red)
	
def main():
    try:
        turtle.TurtleScreen._RUNNING = True
        # get wdth and hgth globally
        turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
        print(turtle.Screen().screensize())
        w = turtle.Screen()
        t = turtle.Turtle()
        t.hideturtle()
        turtle.tracer(0, 0)
        grid(t)
        turtle.update()
        plotCircles(t)
        w.exitonclick()
    finally:
        turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
