import os 
bashcmd = os.system
def getfilefromweb(file):
    if os.name == 'nt':
        bashcmd('curl.exe -O ' + file)
    else:
        bashcmd('wget ' + file)

def downloadfile(file):
    if os.name == 'nt':
        bashcmd('winget install ' + file)
    else:
        bashcmd('sudo apt install ' + file)

def downloadpipfile(file):
    if os.name == 'nt':
        bashcmd('pip install ' + file)
    else:
        bashcmd('sudo apt install ' + file)

def clear():
    if os.name == 'nt':
        bashcmd('cls')
    else:
        bashcmd('clear')