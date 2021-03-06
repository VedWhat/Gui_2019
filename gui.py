#!/usr/bin/python
from Tkinter import *
import cv2
import os
import subprocess
from time import sleep


def digitalcam9():
	os.system("idle-python2.7 -r cam9.py &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)

	proc = subprocess.Popen(["xdotool search --onlyvisible --name cam9"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())

def digitalcam10():
	os.system("idle-python2.7 -r cam10.py &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)

	proc = subprocess.Popen(["xdotool search --onlyvisible --name cam10"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)

	(out, err) = proc.communicate()
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())


def analogcams():
	os.system("idle-python2.7 -r analogcams.py &")


	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	
	#sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())


a = Tk()
a.title("MRM") 																																											
Button(a, text="DigitalCam9", command = digitalcam9, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 0)
Button(a, text="DigitalCam10", command = digitalcam10, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 1)
Button(a, text="AnalogCams", command = analogcams, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 4)


def motorcode():

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	os.system("idle-python2.7 -r tcp_send.py &")
	sleep(1)

	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	#print out
	for i in out.split():
		cmd="xdotool windowsize "+i.strip()+" 532 100 && xdotool windowmove "+i.strip()+" 1366 0 &"
		print cmd
		os.system(cmd)
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	#os.system("xdotool search --onlyvisible --sync --classname --sync --name Python\ 2.7 windowminimize")

Button(a, text="Motorcode", command = motorcode, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=2)

def autonomous():
	 os.system("sudo idle-python2.7 -r autnomRec.py &")
def close():
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	for i in out.split():
		os.system("xdotool windowactivate --sync "+i+" key --clearmodifiers \ --delay 100 alt+F4")

Button(a, text="Autonomous", command = autonomous, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=3)
Button(a, text="Close All", command = close, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 1,column=0)
a.mainloop()

