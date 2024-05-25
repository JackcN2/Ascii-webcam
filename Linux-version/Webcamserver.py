#all the imports
import sys, random, argparse
import numpy as np
import math
import time
from PIL import Image
import cv2
import ctypes
import os
import speech_recognition as sr
import pyttsx3 
import threading
import socket
import threading
import sys



def person():
    personNum = int(input("are you person 1 or 2"))
    if personNum in range(1, 3):
        return(personNum)
        
    else:
        print("try again, invalid value")
        person()
        
        

#start the speech recognizer 
r = sr.Recognizer()
#setting up variables for the file and speech text
file_path = 'out.txt'
recognized_text = ""



print("make sure to keep both scripts in the same directory as they must acess the same file for variables")
print()
print("The other clients ip will be displayed on their screen.")
print()
print("Both of you must open your server first then  client, enter the others ip and pick who is 1 and who is 2")
print()
print("Then press enter on your client to start")
print()

host = input("enter the other persons ip")  # Change this to the host you want to send to

with open("runtimevariables.txt", "w") as file:
    
    if person() == 2:
        file.write("2")
        port = 12344
    else:
        file.write("1")
        port = 12345

    
 # Change this to the port you want to use

#variables for the ascii converter
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '


#file sender function
def send_file_over_socket(file_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(file_path, 'rb') as file:
            data = file.read()
            s.sendall(data)





        

#use this to clear screen after display
def cls():
    os.system('cls' if os.name=='nt' else 'clear')




# convert the image to a numpy array for processing light values
def getAverageL(image):

	"""
	Given PIL Image, return average value of grayscale value
	"""
	# get image as numpy array
	im = np.array(image)

	# get shape
	w,h = im.shape

	# get average
	return np.average(im.reshape(w*h))


    
#main conversion code to put into grayscale
def covertImageToAscii(fileName, cols, scale, moreLevels):
	"""
	Given Image and dims (rows, cols) returns an m*n list of Images 
	"""
	# declare globals
	global gscale1, gscale2

	# open image and convert to grayscale
	image = Image.open(fileName).convert('L')

	# store dimensions
	W, H = image.size[0], image.size[1]
	

	# compute width of tile
	w = W/cols

	# compute tile height based on aspect ratio and scale
	h = w/scale

	# compute number of rows
	rows = int(H/h)
	
	

	# check if image size is too small
	if cols > W or rows > H:
		print("Image too small for specified cols!")
		exit(0)

	# ascii image is a list of character strings
	aimg = []
	# generate list of dimensions
	for j in range(rows):
		y1 = int(j*h)
		y2 = int((j+1)*h)

		# correct last tile
		if j == rows-1:
			y2 = H

		# append an empty string
		aimg.append("")

		for i in range(cols):

			# crop image to tile
			x1 = int(i*w)
			x2 = int((i+1)*w)

			# correct last tile
			if i == cols-1:
				x2 = W

			# crop image to extract tile
			img = image.crop((x1, y1, x2, y2))

			# get average luminance
			avg = int(getAverageL(img))

			# look up ascii char
			if moreLevels:
				gsval = gscale1[int((avg*69)/255)]
			else:
				gsval = gscale2[int((avg*9)/255)]

			# append ascii char to string
			aimg[j] += gsval
	
	# return txt image
	return aimg
    
def set_terminal_title(title):
    # Use an escape sequence to set the terminal title

    sys.stdout.write(f"\033]0;{title}\007")
    sys.stdout.flush()
    
# main() function
def asciiCon():
	
	

	imgFile = ("frame.png")

	# set output file
	outFile = 'out.txt'


	# set scale default as 0.43 which suits
	# a Courier font
	scale = 0.43
	

	# set cols
	cols = 170
	
        
	
	moreLevels = False
	# convert image to ascii txt
	aimg = covertImageToAscii(imgFile, cols, scale, moreLevels)

	# open file
	f = open(outFile, 'w')

	# write to file
	for row in aimg:
		f.write(row + '\n')

	# cleanup
	f.close()
	#print("ASCII art written to %s" % outFile)
	#time.sleep(1/30)
	
	
def cvcap():
        ret, frame = cap.read()
        if not ret:
                print("Camera error")
                

    #Overwrite the png file we use to cache the images for ascii conversion
        cv2.imwrite('frame.png', frame)








#This function formats the text that displays the user audio input and preps it for writing


    

#set the camera I/O
cap = cv2.VideoCapture(0)

# Set the frame width and height, window size, and the speech recognizer
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 540)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=60, cols=170))



# Set the terminal title

set_terminal_title("Your camera:")










# code for calling all the functions and sending it over
while True:
    input()
  #call the camera framecap function
    cvcap()

    #call the function to call the converter with args and write it to file
    asciiCon()
    cls()
    with open(file_path, 'r') as file:
        # Read the lines of the file
        file_lines = file.readlines()
 
        # Print each line
        
        
        for index, line in enumerate(file_lines):
                print(line.strip())
    time.sleep(1/15)
   #send over the txt file we write 
    try:
        send_file_over_socket(file_path, host, port)
    #tell the user if they DC        
    except Exception as e:
            print("Not connected")
    




        

                
