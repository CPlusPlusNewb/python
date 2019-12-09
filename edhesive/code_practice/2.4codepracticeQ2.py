inputt = float(input("Enter a number: "))

#code from (about half way down the page) - https://stackoverflow.com/questions/3886402/how-to-get-numbers-after-decimal-point
if "." in str(inputt):
	print ("."+str(inputt).split(".")[-1])
