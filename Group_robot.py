bool gotkeys = False
bool sound_alarm = False
bool gotjacketorsomethingelse = False
bool dooropen

def getkeys():
    #some code
    gotkeys = True

def sound_alarm():
    #some code
    sound_alarm = True
    
def gotjacketorsomethingelse():
    #some code
    gotjacketorsomethingelse = True
    
def dooropen():
    #some code
    dooropen = True
    
def doorclose():
    #some code
    dooropen = False
    
def program():
    if (gotkeys == False):
    	getkeys()
    if (sound_alarm == False):
        sound_alarm()
    if (gotjacketorsomethingelse == False):
        gotjacketorsomethingelse()
    if (dooropen == False):
        dooropen()
    else if (dooropen == True):
        doorclose()
        

if (__name__ == '__main__'):
    program()
