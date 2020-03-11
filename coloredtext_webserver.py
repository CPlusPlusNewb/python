# almost all code from preston, minus the webserver stuff from mr.coleman / icebowl,
#  and some modifications to that code from noah mcgee. Thanks to them for help
import http.server
import socketserver
import os 
import sys
bashcmd = os.system

'''
def check_for_module(offical_name, module_name):
    installed = False
    try:
        import offical_name
    except ImportError as e:
        bashcmd('sudo apt install ' + module_name)#pass  # module doesn't exist, deal with it.
        bashcmd('clear')
        installed = True
    if (installed == True):
        error('SUCCESS', 'Installed ' + module_name, 'green', False)
'''

def bigline_seperator():
    import colored_text_module as ctm
    ctm.check_for_installs_coltext()
    from colorama import Fore, Back, Style 
    from termcolor import colored, cprint 
    color = 'blue'
    bigline="---------------------------------------"
    text1 = colored(bigline, color, attrs=['bold']) 
    print(text1)
    print(Style.RESET_ALL, end="") 

def main2():
    try:
        try:
            PORT = input("What Port would you like to use?: ")
            PORT = int(PORT)
        except ValueError as e:
            error('ERROR', 'ValueError: Please enter a number, not text', 'red', True)
            main()
        path = '.'
        bigline_seperator()
        error('LIST', 'These are the folders: ', 'green', False)
        files = os.listdir(path)
        #this finds all folders, or anything that doesn't have a period
        for name in files:
            if '.' in name: 
                print ('', end="")
            else:
                print(name)
        bigline_seperator()
        webroot = input("What folder to use as web root?: ")
        try:
            web_dir = os.path.join(os.path.dirname(__file__), webroot)
            os.chdir(web_dir)#web root
            Handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", PORT), Handler)
            print("serving at port", PORT)
            print("Webroot is "+webroot+'/')
            httpd.serve_forever()
            error('SUCCESS', 'setup was successful')
        except FileNotFoundError as e:
            error('ERROR', "FileNotFoundError: that folder does't exsist", 'red', True)
            exit()
    except OSError as e:
        error('ERROR', "OSError: Program will now exit", 'red', True)
        exit()

def main():
    import colored_text_module as ctm
    ctm.check_for_installs_coltext()
    main2()

#error('Success', 'Installed python3-colorama', 'green', False)
#error('Success', 'Installed python3-termcolor', 'green', False)

if (__name__ == "__main__"):
    installed_colored_text_module = False
    try:
        import colored_text_module
    except ImportError as e:
        bashcmd('wget http://10.183.1.20/colored_text_module.py')
        bashcmd('clear')
        installed_colored_text_module = True
    import colored_text_module as ctm
    if (installed_colored_text_module == True):
        ctm.error('SUCCESS', 'Installed colored_text_module.py', 'green', False)
    main()
