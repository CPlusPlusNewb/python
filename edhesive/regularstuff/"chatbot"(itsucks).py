name = input("What is your first name? \n")
#Pascal
last = input("What is your last name? \n")
#Smith
hello = print("Hi there, %s %s, nice to meet you! \n" % (name, last) )

age = int(input("How old are you? \n"))
#17
print("%s is a good age. " % str(age))
if (age >= 16 and age <= 60):
    print("You are old enough to drive. \n")
elif (age > 60):
    print("Your getting old! \n")
else:
    print("You are not old enough to drive. \n")

howru = input("So, %s, how are you today? \n" % name)
#Happy
print("You are %s." % howru)
if (howru == "Happy" or howru == "happy"):
    print("That is good to hear.")
elif (howru == "bad" or howru == "Bad"):
    print("That sucks.")
else:
    print("Thats not good.")
more = input("Tell me more. \n\n")
#I am just happy
print("That's good to hear.\n")

print("Well, %s, it has been nice chatting with you." % name)