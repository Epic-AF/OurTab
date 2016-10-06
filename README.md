# JuanTab
This is like CronTab except it Works! and runs on python. I had a bad expireince with CronTab and felt like making something similer that works.

**For the Raspberry PI**

	1.Open a Terminal.
	2.Type 'sudo apt-get update' 
  	       'sudo apt-get install python'
	3.Type 'sudo nano /etc/rc.local'
	4.Go to the directory you want your file to be in and type "sudo wget https://github.com/juan-pena/JuanTab.git"
	.put "cd /path/to/file && sleep 2 && python juanTab.py" in a line before the 'Exit 0'
	.press ctrl + x then press 'Y' then press enter
	.type 'sudo reboot'
