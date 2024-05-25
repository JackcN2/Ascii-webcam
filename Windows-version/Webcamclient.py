#All the imports
import socket
import time
import os
import ctypes
import sys, random, argparse
from requests import get

#Get current internal ip adress to show the other user
hostname = socket.gethostname()
internal_ip=socket.gethostbyname(hostname)

#Get external ip to show the other user
external_ip = get('https://api.ipify.org').text

#Point the file writer and printer to the correct file
filename = "camcache.txt"

#Print the ip adresses and setup for the script
print("Your external ip is: " +external_ip)
print()
print("Your interal ip is: " +internal_ip)
print()
print("Waiting for connection")
print()

#Functions

#Call to clear the screen between each frame
def cls():
    #cls if on windows, clear if on linux
    os.system('cls' if os.name=='nt' else 'clear')


#Setup the window at the correct size for the ascii image
def set_cmd_window_size(width, height):
    # Define the standard output handle
    STD_OUTPUT_HANDLE = -11
    #Call the win32 api
    h_out = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    # Define COORD structure
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    # Define SMALL_RECT structure
    class SMALL_RECT(ctypes.Structure):
        _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
                    ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

    # Create COORD instance for buffer size
    bufsize = COORD(width, height)
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(h_out, bufsize)

    # Create SMALL_RECT instance for window size
    rect = SMALL_RECT(0, 0, width - 1, height - 1)
    ctypes.windll.kernel32.SetConsoleWindowInfo(h_out, True, ctypes.byref(rect))



#The main  netcode for reciving the image    
def receive_file_over_socket(filename, port):
    
    #This "client" is actually a server as it is the reciving side

    #Bind socket to self (0.0.0.0 is used instead of 127.0.0.1 for cross platform connectivity)
    HOST = "0.0.0.0"

    #Start the connection on our specified port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen(1)
    
        #Accept the connection  from "server"
        conn, addr = s.accept()

        #Open the file we use to cache the image    
        with open(filename, 'wb') as file:
            #While data is incoming
            while True:
                data = conn.recv(1024)
                if not data:
                    #exit loop as the file is finished writing
                    break
                #write data to file
                file.write(data)
        
     




# Change this to the name you want to save the received file as

#wait untill the user presses  enter so  there is no exception of the user  number not existing from the other script
#Also wait to resize the window so the setup process is not confusing for the user
input("Ready?")


#Call the window sizer at the correct  amount of cols and rows                
set_cmd_window_size(170, 60)
#Set the terminal name to tell users wich camera is  theirs and wich camera  isint
ctypes.windll.kernel32.SetConsoleTitleW('Their camera:')


#Set our port
#open the file the server script wrote to
with open('runtimevariables.txt', 'r') as file:

#Read the first character of the file    
    person = file.read(1)
#Set the port to the oposite of what our servers port is
#If  the ports where the same then the client and server would just display the same thing
if person == "1":
    port = 12344
elif person == "2":
    port = 12345

#The main reciver loop
while True:
    #Recive the text file from the server
    receive_file_over_socket(filename, port)
    #Clear the screen in  preparation
    cls()
    #Open the recived file
    with open(filename, 'r') as file:
        # Read the lines of the file
        file_lines = file.readlines()
 
        # Print each line
        for index, line in enumerate(file_lines):
            print(line.strip())
                
