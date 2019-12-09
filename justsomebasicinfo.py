import os
import subprocess
import socket
import getpass
import datetime
import shutil
import memory
from importlib import reload
import time
#import keyboard#i give up on keyboard module, ffs
import decimal

today = datetime.date.today()
total, used, free = shutil.disk_usage("/")

from threading import Timer

class InfiniteTimer():
    """A Timer class that does not stop, unless you want it to."""

    def __init__(self, seconds, target):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.
            self.thread = Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
        else:
            print("Timer already started or running, please wait if you're restarting.")

    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize.")


def ipaadress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#not meh code. https://stackoverflow.com/a/25850698
	s.connect(("8.8.8.8", 80))#not meh code. https://stackoverflow.com/a/25850698
	print("| ip adress:                    " + str(s.getsockname()[0]) + "           |")#not meh code. https://stackoverflow.com/a/25850698
	s.close()#not meh code. https://stackoverflow.com/a/25850698

bruh4 = ""
d = ""

def num_after_point(x):#NOT MEH CODE: https://stackoverflow.com/a/35586226
    s = str(x)#NOT MEH CODE: https://stackoverflow.com/a/35586226
    if not '.' in s:#NOT MEH CODE: https://stackoverflow.com/a/35586226
        return 0#NOT MEH CODE: https://stackoverflow.com/a/35586226
    return len(s) - s.index('.') - 1#NOT MEH CODE: https://stackoverflow.com/a/35586226

def cpuspacecheck():
    global bruh4
    global d
    d = num_after_point(float(memory.CPU_Pct))
    if (10.0 > float(memory.CPU_Pct) >= 1.0):
        if (d == 1):
            bruh4 = "  "
        elif (d == 2):
            bruh4 = " "
        elif (d == 0):
            bruh4 = ""
    elif (100.0 >= float(memory.CPU_Pct) >= 10.0):#if its higher then 100, idk how you could use more then 100% of the cpu, NGL
        if (d == 1):
            bruh4 = " "
        elif (d == 2):
            bruh4 = ""

x = ""
y = ""
z = ""

def memoryspacecheck():
    global x, y, z
    if (10000 > float(memory.mem_T) >= 10):
        x = " "
    elif (100000 > float(memory.mem_T) >= 10000):
        x = ""
    
    if (10000 > float(memory.mem_U) >= 10):
        y = " "
    elif (100000 > float(memory.mem_U) >= 10000):
        y = ""

    if (10000 > float(memory.mem_F) >= 10):
        z = " "
    elif (100000 > float(memory.mem_F) >= 10000):
        z = ""
bruh = ""
bruh2 = ""
bruh3 = ""
def stoargespacecheck():
    global bruh
    global bruh2
    global bruh3
    if (10 > (total // (2**30)) >= 1):
        bruh = "   "
    elif (100 > (total // (2**30)) >= 10):
        bruh = "  "
    elif (1000 > (total // (2**30)) >= 100):
        bruh = " "
    else:
        bruh = ""

    if (10 > (used // (2**30)) >= 1):
        bruh2 = "   "
    elif (100 > (used // (2**30)) >= 10):
        bruh2 = "  "
    elif (1000 > (used // (2**30)) >= 100):
        bruh2 = " "
    else:
        bruh2 = ""

    if (10 > (free // (2**30)) >= 1):
        bruh3 = "   "
    elif (100 > (free // (2**30)) >= 10):
        bruh3 = "  "
    elif (1000 > (free // (2**30)) >= 100):
        bruh3 = " "
    else:
        bruh3 = ""

def spacing_checks():
    memoryspacecheck()
    cpuspacecheck()
    stoargespacecheck()

def main():
    spacing_checks()
    global bruh, bruh4
    global d
    global x, y, z
    os.system("clear")
    #=====================================================: 53
    print ("|==================some basic info====================|")
    hostname = socket.gethostname()    
    ipaadress() #not meh code.
    print ("| computer Host name:           " + hostname + "                |")
    print ("| Fully qualified name:         " + socket.getfqdn(socket.gethostname()) + "        |")#this was just looking at the socket module, this looked interesting
    #print ("Computer UID (User ID): " + str(os.getuid())) #this is kind of dumb, ngl
    if (str(getpass.getuser()) == "root"):
        print ("| Username:                     " + getpass.getuser() + "                  |")
    else:
        usernamelangth = len(getpass.getuser())
        if (21 >= usernamelangth > 0):
            print ("| Username:                     " + getpass.getuser() + "        |")#found the getpass module on : https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
            print ("|                               Hello " + getpass.getuser() + "! |")
        elif (usernamelangth <= 21):
            print ("| Username:                                   |")#this is from my project reading and writing.
            p = 51 - usernamelangth
            craig = ""
            for i in range (0, p):
                craig += " "
            print ("| " + getpass.getuser() + craig + " |")
            print ("|                               Hello " + getpass.getuser() + "! |")
        else:
            print ("| Username:                     " + "Too Long!" + "             |")#this is from my project reading and writing.
    getxwdlength = len(os.getcwd())
    if (22 >= getxwdlength > 0):
        print ("| The current directory is:    " + os.getcwd() + "   |")#this is from my project reading and writing.
    elif (getxwdlength <= 22):
        print ("| The current directory is:                           |")#this is from my project reading and writing.
        p = 51 - getxwdlength
        craig = ""
        for i in range (0, p):
            craig += " "
        print ("| " + os.getcwd() + craig + " |")
    else:
        print ("| The current directory is:     " + "Too Long!" + "             |")#this is from my project reading and writing.
    print ("| Date:                         " + today.strftime('%d, %b %Y') + "          |")#this is from my project reading and writing.
    print ("|==================Hard drive info====================|")
    print ("| Total:                        %d gb" % (total // (2**30)) + bruh + "               |")
    print ("| Used:                         %d gb" % (used // (2**30)) + bruh2 + "               |")
    print ("| Free:                         %d gb" % (free // (2**30)) + bruh3 + "               |")
    print ("|====================Memory info======================|")
    print ('| Total:                        '+ str(memory.mem_T) + ' Mb ' + x + '             |')
    print ('| Used:                         ' + str(memory.mem_U) +' Mb ' + y + '             |')
    print ('| Free:                         ' + str(memory.mem_F) +' Mb ' + z + '             |')
    print ("|=====================CPU info========================|")
    print ("| Usage:                        " + memory.CPU_Pct + "% " + bruh4 + "               |")
    print ("|=========Close this tab to close the program=========|")
    print(z)
    
    #print ("|==========================|==========================|")
  #  print ('''|⠀  ⠰⡿⠿⠛⠛⠻⠿⣷               |
#| ⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀     |
#|⠀ ⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷    |
#| ⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇      |
#| ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁       |
#| ⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀          |
#| ⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗         |
#| ⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄       |
#| ⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃       |
#| ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄            |
#| ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁            |
#| ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁            |
#| ⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟             |
#| ⠀⠀⠀⠀⠀⠉⠉⠉                 |''')
#    print ("|==========================|")#after this, its just enough space for the one line to type again    
#import threading 
#import imp

def tick():
    #if keyboard.read_key() != "s":
    reload(memory)
    main()
        #keyboard.unhook_all()
    
if (__name__ == "__main__"):
    #main()
    #print ('This is for the "Keyboard" module needed to detect if you click s \nto close the refreshing of the program, \nas the "Keyboard" module does not come standard with python. \nPlease Enter your sudo password') 
    #os.system("su -")
    #os.system("sudo apt-get install python-pip python-dev build-essential")
    #os.system("pip3 install keyboard")
    t = InfiniteTimer(0.1, tick)
    t.start()
    #if keyboard.press_and_release('s, space'):
    #    t.close()