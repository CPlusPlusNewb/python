import os
import subprocess
import socket
import getpass

#code from noah mcgee, modified to work with my code, thanks :)
def main():
	os.system("mkdir rockybruhsyear1project")
	os.system("mkdir rockybruhsyear1project/Ezekielsfullcode")
	os.system("mkdir rockybruhsyear1project/Shanesfullcode")
	os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/Ezekielscode.py")#thanks noah for this code, with some modifications to work for what i need
	os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/need.py")#thanks noah for this code
	os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/Prestonscode.py")#thanks noah for this code
	os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/Shanescode.py")#thanks noah for this code
	os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/yearoneprojectDRIVER.py")#thanks noah for this code
	os.system("cd rockybruhsyear1project/Ezekielsfullcode;wget https://raw.githubusercontent.com/EzekielBorms/python2019/master/Python%20Git/first%20turtle.py")#thanks noah for this code
	os.system("cd rockybruhsyear1project/Shanesfullcode;wget https://raw.githubusercontent.com/thormiller/python/master/mike.py")#thanks noah for this code
	#os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/text.txt")
	run()
	
def ipaadress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#not meh code. https://stackoverflow.com/a/25850698
	s.connect(("8.8.8.8", 80))#not meh code. https://stackoverflow.com/a/25850698
	print(s.getsockname()[0])#not meh code. https://stackoverflow.com/a/25850698
	s.close()#not meh code. https://stackoverflow.com/a/25850698

def run():
	
	os.system("clear")
	hostname = socket.gethostname()    
	ipaadress() #not meh code.
	print ("computer Host name: " + hostname)
	print ("Fully qualified name: " + socket.getfqdn(socket.gethostname()))#this was just looking at the socket module, this looked interesting
	path = os.getcwd()
	#print ("Computer UID (User ID): " + str(os.getuid())) #this is kind of dumb, ngl
	print ("Username: " + getpass.getuser())#found the getpass module on : https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
	print ("The current directory is %s" % path)#this is from my project reading and writing.
	#print ("\n")
	a = input ("Would you like to run the group python project? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("python3 " + path + "/rockybruhsyear1project/yearoneprojectDRIVER.py")
	elif (a == "N" or a == "n"):
		exit()
	else:
		run()

if (__name__ == "__main__"):
	main()
