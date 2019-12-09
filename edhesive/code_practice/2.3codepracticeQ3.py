# your code goes here #FROM https://github.com/icebowl/python/blob/master/edhesive/2.3.3.py WITH SOME MINOR MODIFACTIONS
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))

totalminutes = (60*hours) + minutes
totalminutes += 15

newhour = int(totalminutes / 60)
newminute = int(totalminutes % 60)

while(newhour > 12):
    newhour -= 12

print("Hours: "+str(newhour))
print("Minutes: "+str(newminute))
