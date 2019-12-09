r = int(input("Enter the red: "))
g = int(input("Enter the green: "))
b = int(input("Enter the blue: "))

correct = True

if (r > 255 or r < 0):
	print("Red number is not correct.")
	correct = False
if (g > 255 or g < 0):
	print("Green number is not correct.")
	correct = False
if (b > 255 or b < 0):
	print("Blue number is not correct.")
	correct = False
	
if (correct == True):
	print("No Output")