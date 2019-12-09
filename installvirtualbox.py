import os

def main():
    os.system("cd /Downloads/; wget http://10.183.1.26/downloads/virtualBox/virtualbox-6.0_6.0.14-133895~Debian~buster_amd64.deb")
    os.system("sudo dpkg -i virtual*.deb")
	#os.system("cd rockybruhsyear1project/;wget http://10.183.1.13/python/turtle/yearoneproject/text.txt")


if (__name__ == "__main__"):
	main()