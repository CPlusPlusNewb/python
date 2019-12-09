Numer = int(input("Numerator: "))
Denom = int(input("Denominator: "))

if (Denom == 0):
	print("Error - cannot divide by zero.")
else:
	print("Decimal: " + str(Numer / Denom))