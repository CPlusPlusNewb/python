#pn / cplusplusnewb
# d(dividend), q(quotent), r(remainder)
def hexcon(num):
	key = "0123456789ABCDEF" #hex key, thanks to kenny
	h = ""
	h16 = int(num / 16)
	h1 = num % 16
	h = key[h16] + key[h1]
	return h
	
def reversehexcon(num):
	res = int(num, 16) 
	return res

#================================

def BinarytoDecimal(binary):#this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  
  binary1 = binary                      #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  decimal, i, n = 0, 0, 0               #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  while(binary != 0):                   #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    dec = binary % 10                   #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    decimal = decimal + dec * pow(2, i) #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    binary = binary//10                 #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
    i += 1                              #this is from https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/ MUCH THANKS :D
  print("\n==============================")
  print("decimal = " + str(decimal), end = " ")
  hs = hexcon(decimal)
  print("hex = " + str(hs))
  print("==============================\n")
  

  #os.system("echo '%s' | pbcopy" % decimal)
  #print("Copied to clipboard!") 
def damain():
	inpt = input("Decimal, Binary, or Hex input? (d/b/h) :")
	if (inpt == "b"):
		b = int(input("Da binary number : "))
		BinarytoDecimal(b) 
	elif (inpt == "d"):
		n = int(input("Input an interger < 256: "))
		d = 128
		n_original = n
		binString = ""
		#================================
		for i in range (0,8):
			q = int(n / d)
			r = int(n % d)
			n = r
			d = int(d / 2)
			binString = binString + str(q)
			if(i == 3):
				binString += " "
		print("\n==============================")
		print("bin = " + binString, end = ", ")
		hs = hexcon(n_original)
		print("hex = " + hs)
		print("==============================\n")
	elif (inpt == "h"):
		bruh_orgianal = input("Da hex number : ")
		decimal_thing = reversehexcon(bruh_orgianal)
		n = decimal_thing
		d = 128
		n_original = n
		binString = ""
		#================================
		for i in range (0,8):
			q = int(n / d)
			r = int(n % d)
			n = r
			d = int(d / 2)
			binString = binString + str(q)
			if(i == 3):
				binString += " "
		print("\n==============================")
		print("bin = " + binString, end = ", ")
		print("decimal = " + str(decimal_thing))
		print("==============================\n")
	else:
		print('please input "d" or "b"')
		damain()

damain()
