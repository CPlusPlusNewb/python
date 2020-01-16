def main():
	a = int(input("Enter a number: "))
	oldi = a
	if (a > oldi):
		print("Largest: " + str(a))
		oldi = a
	else:
		print("Largest: " + str(oldi))

	for i in range (0, 5):
		a = int(input("Enter a number: "))
		if (a > oldi):
			print("Largest: " + str(a))
			oldi = a
		else:
			print("Largest: " + str(oldi))

main()
