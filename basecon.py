#basecon.py pn

def bincon(num, addspace):
	n = num
	s = addspace
	#print(n, s)
	#print(n, end = " = ")
	d = 128
	binString = ""
	for i in range (0,8):
		q = int(n / d)
		r = int(n % d)
		#where old code not needed was at
		n = r
		d = int(d / 2)
		binString = binString + str(q)
		if(s == 1 and i == 3):
			binString += " "
	#print(binString)
	return binString

def main(addaspacemaybe):
	#num = "151"
	bs = ""
	for i in range(0,256):
		#bs = bincon(i, bs)
		#print(i, bs)
		bs = bincon(i, addaspacemaybe)
		print(str(i) + " =", str(bs))
#tingy i added
def ting():
	aspaceting = input("Do you want a nice l1l space (y/n)? ")#who knows, maybe they dont
	space = 0
	if(aspaceting == "y" or aspaceting == "n" or aspaceting == "Y" or aspaceting == "N"):
		if (aspaceting == "y"):
			space = 1
			main(space)
		else:
			space = 0
			main(space)
	else:
		print("Please spell it correctly :D")#, end = " ")
		ting()
		
ting()
#addaspace = " "
#bincon(number, addaspace)
#IDK WHY WE DONT JUST USE BINCON HERE, but just following instructions
