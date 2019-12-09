import ipaddress
#not my code, but wanted it for class
def main():
    IP = input("Input an ipadress: ")
    ip2bin =  ".".join(map(str,["{0:08b}".format(int(x)) for x in IP.split(".")]))#not my code
    print(ip2bin)#not my code
	

if (__name__ == "__main__"):
    main()