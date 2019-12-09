#this is preston's code

import random
x = ""
def maf_function(anumber, asecondnumber, Math, Mathkind, NAMEofanumber, NAMEofasencondnumber):
  if (Math == "maf" or Math == "Maf"):
      if (Mathkind == "+"):
        print (NAMEofanumber + " + " + NAMEofasencondnumber, end = " = ")
        print (anumber + asecondnumber)
      elif (Mathkind == "-"):
        print (NAMEofanumber + " - " + NAMEofasencondnumber, end = " = ")
        print (anumber - asecondnumber)
      elif (Mathkind == "*"):
        print (NAMEofanumber + " * " + NAMEofasencondnumber, end = " = ")
        print (anumber * asecondnumber)
      elif (Mathkind == "/"):
        print (NAMEofanumber + " / " + NAMEofasencondnumber, end = " = ")
        print (anumber / asecondnumber)
  else:
    if (anumber > asecondnumber):
      print(anumber + " > " + asecondnumber)
    elif (anumber == asecondnumber):
      print(anumber + " = " + asecondnumber)
    else:
     print(anumber + " < " + asecondnumber)
    
  print("This is a newbs first function, \nplz go ez.")
  
  
def dice_game():
  min = 1
  y = int(input("How many sides (max 100): "))
  max = y
  print ("Rolling the die...\n")
  print ("The values are", end =", ")
  print (random.randint(min, max))
  print ("and", end =", ")
  print (random.randint(min, max)) 
  roll_again = input("\nRoll the dices again? (y/n)")
  if (roll_again == "y"):
    dice_game()
    
def coinflip_game():
  bruh = ""
  bruhbutword = ""
  guess = input("Heads or Tails (h/t): ")
  print ("Flipping...")
  flip = random.randint(0, 1)
  if (flip == 0):
    bruh = "t"
    bruhbutword = "Tails"
  else:
    bruh = "h"
    bruhbutword = "Heads"
  if (guess == bruh):
    print("You were right! it's, " + bruhbutword)
  elif (guess != bruh):
    print ("OUCHIE, it was " + bruhbutword)
  else:
    print ("\nSomething went wrong")
  flipagain = input("Re-Flip? (y/n)")
  if (flipagain == "y"):
    coinflip_game()
  
'''
this code goes in this order of inputs:
1. input name, outputs name
2. askes what you want to do, maf, game, or comparison
3. base on what you chose it could
 a. goto the function for one of the games you can chose from
 b. goto the function for the maf function
 c. goto the function for the comparison function
4. if you chose a game it askes if you wanna do it again or
5. exit
'''

'''
p = anumber for maf or comparison
n = asecondnumber for maf or comparison
d = if (maf or Maf) do \/
e = Mathkind +, - *, /
b = NAMEofanumber string for anumber, im dumb and didn't know how to str()
c = NAMEofasencondnumber string for asecondnumber, im dumb and didn't know how to str()
'''

'''
outputs:
dice: outputs the 2 sides and asks if you wanna do it again
coin flip: outputs either head or tails and what you got, then asks if you wanna do it again
maf: outputs the value
comparison: outputs >, <, =
'''
a = input("Enter your name : ") 
print("Hello " + a + "!")
d = input("Maf, or Comparison or a game?: ") 

if (d == "maf" or d == "Maf"):
  e = input("What kind of maf (+, -, /, *): ") 
  b = input("Enter a number : ")
  p = int(b)
  if (b == ""):
   print("Please enter something")
   b = input("Enter a number : ")
   p = int(b)

  c = input("Enter a second number : ")
  n = int(c)
  if (c == ""):
   print("Please enter something")
   c = input("Enter a second number : ")
   n = int(c)
 
elif (d == ""):
  print("Please enter something")
  d = input("Maf, or Comparison or a game?: ") 
  
elif (d == "a game" or d == "A game" or d == "a Game" or d == "A Game" or d == "Game" or d == "game"):
  x = input("Dice or Coin flip?: ")
  if (x == "Dice" or x == "dice"):
    dice_game()
      
  elif (x == "Coin flip" or x == "coin flip" or x == "Coin Flip"):
    coinflip_game()
    
elif (d == "Comparison" or d == "comparison"):
  p = input("Enter a number : ")
  if (p == ""):
   print("Please enter something")
   p = input("Enter a number : ")
   
  n = input("Enter a second number : ")
  if (n == ""):
   print("Please enter something")
   n = input("Enter a second number : ")
  c = ""
  b = ""
elif (d != "Maf" or d != "maf" or d != "Comparison" or d != "comparison" or d != "a game" or d != "A game" or d != "a Game" or d != "A Game" or d != "Game" or d != "game"):
  print("Please spell it correctly")
  d = input("Maf, or Comparison or a game?: ")
  p = ""
else:
  e = "" 
  p = ""
  n = ""
if (d == "Maf" or d == "maf" or d == "Comparison" or d == "comparison"):
  maf_function(p, n, d, e, b, c)
  
  
  
  
  
  
  
  
  
#this is preston's code
