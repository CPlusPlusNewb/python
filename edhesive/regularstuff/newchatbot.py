import random

q1 = input("This is question 1: ")
q2 = input("This is question 2: ")
q3 = input("This is question 3: ")
q4 = input("This is question 4: ")
q5 = input("This is question 5: ")

if (q1 == 1 or q2 == 1 or q3 == 1 or q4 == 1 or q5 == 1):
    print("YOU ARE ROBOT NUMBER 1!")
elif (q1 == 2 or q2 == 2 or q3 == 2 or q4 == 2 or q5 == 2):
    print("YOU ARE ROBOT NUMBER 2!")
elif (q1 == 3 or q2 == 3 or q3 == 3 or q4 == 3 or q5 == 3):
    print("YOU ARE ROBOT NUMBER 3!")
else:
    if (q1 == " "):
        print("heckyeah")
    elif (q1 == "bruh"):
        print("heckheah")
    else:
        print("bruh1?")
        print(random.randint(0, 10))