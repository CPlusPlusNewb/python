#pn 

#question9:
print ("Twinkle, \ttwinkle, \tlittle star")

#question11:
x = input ("Enter a number (assume its 5): ")
y = input ("Enter a number (assume its 4): ")
print ("Values: " + x + y)

#question12:
x = "apple"
y = x
z = "banana"
print (x + " " + y + "\n" + z)

#question13:
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
#ansewer1 #TypeError: can only concatenate str (not "int") to str #dosn't work
#print("The answer is: " + int(n1+n2))
#ansewer2
print("The answer is: " + str(n1+n2))
#ansewer3 #TypeError: can only concatenate str (not "int") to str #dosn't work
#print("The answer is: " + int(n1+n2))
#ansewer4
print("The answer is: " + str(n1+n2))

#question15:
print ("computer" + "science")

#question18
def ansewr():
	print("I know there's a proverb which that says")
	print('"To err is human,"')
	print("but")
	print("a human error is nothing to what a computer")
	print("an do if it tries.")

	print("- Agatha Christie")

def ansewer1():
	quote = "\"To err is human,\""
	print ("I know there's a proverb which that says \n"+ quote + "\nbut")
	print ("a human error is nothing to what a computer")
	print ("can do if it tries.\n\n- Agatha Christie")
	
def ansewer2():
	quote = "\"To err is human,\""
	print ("I know there's a proverb which that says \t"+ quote + "\tbut")
	print ("a human error is nothing to what a computer")
	print ("can do if it tries.\t\t- Agatha Christie")
	
def ansewer3():
	quote = "\"To err is human,\""
	print ("I know there's a proverb which that says \n + quote + \nbut")
	print ("a human error is nothing to what a computer")
	print ("can do if it tries.\n\n- Agatha Christie")
	
def ansewer4():
	quote = "To err is human,"
	print ("I know there's a proverb which that says \n"+ quote + "\nbut")
	print ("a human error is nothing to what a computer")
	print ("can do if it tries.\n\n- Agatha Christie")
	
if ansewer1() == ansewr():
	print("Its number 1")
elif ansewer2() == ansewr():
	print("Its number 2")
elif ansewer3() == ansewr():
	print("Its number 3")
elif ansewer4() == ansewr():
	print("Its number 4")
