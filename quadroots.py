def roots(a, b, c):
	D = (b*b - 4*a*c)
	print("\nD = " + str(D))
	if(D >= 0):
		print("REAL ROOTS")
		D = D**0.5
		x1 = (-b + D) / (2 * a)
		x2 = (-b - D) / (2 * a)
		print("x1 = " + str(x1) + "\nx2 = " + str(x2))
	elif(D < 0):
		D = (D * -1)**0.5
		print("IMAGINARY ROOTS")
		print("x1 = " + str(b/(2 * a)) + " - " + str(D/(2 * a)) + "i")
		print("x1 = " + str(b/(2 * a)) + " + " + str(D/(2 * a)) + "i")

if __name__ == '__main__':
	print("input a, b, and c for the quadratic (ax^2 + bx + c)")
	a = input("Enter a: ")
	b = input("Enter b: ")
	c = input("Enter c: ")
	roots(float(a), float(b), float(c))
'''
input a, b, and c for the quadratic (ax^2 + bx + c)
Enter a: 5
Enter b: 4
Enter c: 2

D = -24.0
IMAGINARY ROOTS
x1 = 0.4 - 0.4898979485566356i
x1 = 0.4 + 0.4898979485566356i
'''
