#bincon_loop.py  pn
#orginal code by cwc
# d(dividend), q(quotent), r(remainder)
#================================
n = int(input("Input an interger < 256: "))
d = 128
n_original = n
binString = ""
#================================
for i in range (0,8):
  q = int(n / d)
  r = int(n % d)
  print ("dividend", end = " = ")#changes made by PN
  print (d, end = ", ")#changes made by PN
  print ("quotent", end = " = ")#changes made by PN
  print (q, end = ", ")#changes made by PN
  print ("remainder", end = " = ")#changes made by PN
  print (r)#changes made by PN
  n = r
  d = int(d / 2)
  binString = binString+str(q)
print("\n==============================\n")
print
print(str(n_original) + " in base 10 = " + binString + " base 2")
print("\n==============================")
