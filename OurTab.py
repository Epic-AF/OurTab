#~Imports~#
import time
import os

'''
This is a very simple program with a simple purpose. To Mother Fuckin Work. If you are running on the raspberry pi follow this commands to start the script on startup.
1.'sudo nano /etc/rc.local'.as you see there is some stuff there.
2.put "cd /path/to/file && sleep 2 && python juanTab.py" in a line before the 'Exit 0'

 
This part is to show you how to Config the script. if you need it to just start a counted number of times set count to 'True' or if you want it to run the comand infinite amount of leave count at 'False'

Modes
Infinte Mode = a mode that means the command has no set limt of times if will be exacutied, but can have either a few seconde delays or even days || To use this mode make sure that "count" is equal to "False"
Counted Mode = a mode that makes sure your command is only ran a counted number of time for example haveing it run 8 times || To use this mode make sure "count" is equal to "True" then make sure "num" is equal to the amount of times you would like it to run



'''


count = False
num = 0 #~change 0 to the amount of times you wount the program to run it~#

delay = 0 #~the amount of time between the command being run goes here. ONLY FUNCTIONAL IF IN INFINITE MODE! ~#

atreboot = False

#~If you set these to 0 it will continue doing the command~#
sec = 0
minute = 0
hour = 0
day = 0

com = 'Put your command here' #~this is where your command goes~#

total = (sec)+(minute*60)+(hour*3600)+(day*86,400)
if count == true:
    for i in range(num+1):
        time.sleep(total)
        os.system(com)

else:
    while True:
        time.sleep(total)
        os.system(com)

'''
Made By Juan Pena
Instagram = @juanisdatboi
'''
