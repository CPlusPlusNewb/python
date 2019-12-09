a = input("How many bottom numbers?: ")
if (a == "1" or a == "2" or a == "3"):
  a1 = int(input("Enter the bottom number 1: "))
# APERITNLY these arnt needed, it'll crash, pretty much telling the user,
# "HEY! enter a base10 number! dummy ;)"

#  if (a1 == ""):
#    print("Please enter a number")
#    a1 = int(input("Enter the bottom number 3: "))
if (a == "2" or a == "3"):
  b2 = int(input("Enter the bottom number 2: ")) 
#  if (b2 == ""):
#    print("Please enter a number")
#    b2 = int(input("Enter the bottom number 3: "))
if (a == "3"):
  c3 = int(input("Enter the bottom number 3: "))
#  if (c3 == ""):
#    print("Please enter a number")
#    c3 = int(input("Enter the bottom number 3: "))

if (a == "1"):
  print (1/(1/a1))
elif (a == "2"):
  print (1/(1/a1 + 1/b2))
else:
  print (1/(1/a1 + 1/b2 + 1/c3))
