#NOT MY CODE, but wanted it for maf
#UPDATE: made some minor changes to suit my needs, by adding a print for what it wants you to input, and
#adding the imaginary numbers to the output, they may not be correct but idgaf
import math

print("input a, b, and c for the quadratic (ax^2 + bx + c)")
a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

d = b**2-4*a*c # discriminant
D = (b*b - 4*a*c)

if d < 0:
	D = (D * -1)**0.5
	print ("This equation has no real solution")
	print(str(b/(2 * a)) + " - " + str(D/(2 * a)) + "i")
	print(str(b/(2 * a)) + " + " + str(D/(2 * a)) + "i")
elif d == 0:
	x = (-b+math.sqrt(b**2-4*a*c))/2*a
	print ("This equation has one solutions: " + str(x))
else:
	x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
	x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
	print ("This equation has two solutions: ", x1, " or", x2)
