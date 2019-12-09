month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

if (month == 9):
    if (day > 15):
        print ("Second half of the month")
    else:
        print ("First half of the month")
else:
    print ("Not in September")