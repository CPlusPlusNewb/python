total = 0
totalnums = 0
while (total <= 100):
    num = int(input("Enter a number: "))
    totalnums += 1
    total += num
print("\nSum: " + str(total))
print("Numbers Entered: " + str(totalnums))