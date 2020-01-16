petnum = 0
pet = input("What pet do you have? ")
while (pet != "rock"):
    petnum += 1
    print("You have a " + pet + " with a total of " + str(petnum) + " pet(s)")
    pet = input("What pet do you have? ")