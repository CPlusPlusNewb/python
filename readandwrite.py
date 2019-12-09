import os
import urllib.request
import shutil
	
#==========got this from some website, im writing this multiple days later, so just note, i only added the input parts to make it work with the rest of the program.=============
def getthefile(url, name, path):
	f= open(path + name,"w+")
	with urllib.request.urlopen(url) as response:
		html = response.read()
		f.write(str(html))
		print("Successfully created the file " + name)
	
	f.close()
#===================================
def main():
	path = os.getcwd() + "/http/pythoon/"
	
	#this srewd me over, i hate it now, it deleted all my home directory while messing with making it so you can input stuff to take >=(
	#shutil.rmtree(path)#this is for me when im testing it so i dont have to delete it everytime :)
	
	try:#===========got this from some website, im writing this multiple days later, so just note that.============
		os.mkdir(path)
	except OSError:
		print ("Creation of the directory %s failed" % path, "\n this might be becuase it already exsits")
	else:
		print ("Successfully created the directory %s " % path)
		#================
	#==========got this from some website, im writing this multiple days later, so just note, i only added the input parts to make it work with the rest of the program.==========
	
	getthefile("https://github.com/CPlusPlusNewb/python/archive/master.zip", "style.css", path)
	getthefile("http://[IP ADDRESS REDACTED]/html/index.html", "index.html", path)
	
	#===========================

def main2():

	# detect the current working directory and print it
	path = os.getcwd()#didn't make this either
	print ("The current directory is %s" % path + "\n")

main2()

d = input("are you in the home directory? (y/n) ")
if (d == "y"):
	if (__name__ == "__main__"):
		main()
else:
	print("Please be in the home directory")
