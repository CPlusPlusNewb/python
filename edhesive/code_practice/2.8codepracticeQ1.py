firstnum = int(input("Enter a number: "))#20
secondnum = int(input("Enter a number: "))#50
thirdnum = int(input("Enter a number: "))#5

if (firstnum > secondnum and firstnum > thirdnum):
	print("Largest: " + str(firstnum))
elif (secondnum > firstnum and secondnum > thirdnum):
	print("Largest: " + str(secondnum))
elif (thirdnum > secondnum and thirdnum > firstnum):
	print("Largest: " + str(thirdnum))
elif (firstnum == secondnum):
	print(str(firstnum) + " = " + str(secondnum))
elif (thirdnum == firstnum):
	print(str(firstnum) + " = " + str(thirdnum))
elif (thirdnum == secondnum):
	print(str(secondnum) + " = " + str(thirdnum))
