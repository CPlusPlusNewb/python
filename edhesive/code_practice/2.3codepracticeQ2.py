feet1 = int(input("Enter the Feet for the first piece of fabric: "))#3
inches1 = int(input("Enter the Inches for the first piece of fabric: "))#11

feet2 = int(input("Enter the Feet for the second piece of fabric: "))#2
inches2 = int(input("Enter the Inches for the second piece of fabric: "))#5

feet = feet1 + feet2
inches = inches1 + inches2

while inches > 12:
	feet += 1
	inches -= 12

print("Feet: " + str(feet) +" Inches: " + str(inches))
