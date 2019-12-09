import os 

def BinarytoDecimal(binary):#this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  
  binary1 = binary                      #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  decimal, i, n = 0, 0, 0               #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  while(binary != 0):                   #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    dec = binary % 10                   #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    decimal = decimal + dec * pow(2, i) #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    binary = binary//10                 #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    i += 1                              #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  print(decimal)                        #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  

  #os.system("echo '%s' | pbcopy" % decimal)
  #print("Copied to clipboard!") 

a = input("Decimal or binary input? (d/b) :")
if (a == "d"):
  d = int(input("All decimal numbers : "))
  for i in range (0,d):#he made us do repeating stuff
    b = int(input("Da decimal number : "))
    bruh = bin(b).replace("0b","") #the "bin()" command i learned in class
#thanks too the people from before for the .replace, IDK how
#to replace it for what i needed, which was just the numbers
    print (str(b) + " in Binary is : " + bruh)
  
  #os.system("echo '%s' | pbcopy" % bruh)
  #print("Copied to clipboard!") 
elif ( a == "b"):
  b = int(input("Da binary number : "))
  BinarytoDecimal(b) 
