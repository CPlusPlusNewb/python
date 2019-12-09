#num = int(input("Enter a number: "))
for i in range (0, 4):#
    num = 0
    if (i == 0):
        num = 5
        print("With a input of 5: ")
    elif (i == 1):
        num = 26
        print("With a input of 26: ")
    elif (i == 2):
        num = 3
        print("With a input of 3: ")
    elif (i == 3):
        num = 48
        print("With a input of 48: ")
    num = num % 4
    if (num == 1):
        print ("A")
    elif (num == 2):
        print ("B")
    elif (num == 3):
        print ("C")
    elif (num == 4):
        print ("D")
    else:
        print ("E")