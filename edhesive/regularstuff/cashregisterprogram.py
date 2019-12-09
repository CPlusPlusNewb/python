#thigs you may not know that i learned \/
#the round funtion, sytax: round(number, digits)
#the replace function, sytax: string.replace(old, new, count)

def notenoughmoney(allprice, inputmoney):
	owe = round(inputmoney - allprice, 2)
	bruh = "They owe you $" + str(owe) + " still"
	print(bruh.replace('-', ''))

def toomuchmoney(allprice, inputmoney):
	change = round(allprice - inputmoney, 2)
	bruh = "You owe them $" + str(change) + " still"
	print(bruh.replace('-', ''))

print('\ninput in format: "2.12" for 2 dollars and 12 cents')
oneitem = float(input("First item price: "))
twoitem = float(input("Second item price: "))
threeitem = float(input("Third item price: "))

allitemprice = round(oneitem + twoitem + threeitem, 2)
print(allitemprice)

moneyinput = float(input("What their total payment is: "))

if (allitemprice == moneyinput):
	print("No money back")
	
elif (allitemprice > moneyinput):
	notenoughmoney(allitemprice, moneyinput)
	
elif (allitemprice < moneyinput):
	toomuchmoney(allitemprice, moneyinput)
	
else:
	print("ERROR!")
