#keys.py Kenny PN
key = "0123456789abcdef"
for i in range (1,16):
	print(key[i]," ",end = "")

h16 = 9
h1 = 13
print("\n**************************")
print(h16*16+h1)
print(key[h16], key[h1])
