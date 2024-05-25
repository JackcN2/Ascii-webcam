#All the imports
import socket
import time
import os
import ctypes
import sys, random, argparse
from requests import get

#Get current internal ip adress to show the other user
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
   
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
        return IP


#Point the file writer and printer to the correct file
filename = "camcache.txt"

#Get external ip to show the other user
external_ip = get('https://api.ipify.org').text

#Point the file writer and printer to the correct file
filename = "camcache.txt"

#Print the ip adresses and setup for the script
print("Your external ip is: " +external_ip)
print()
print("Your interal ip is: " +get_ip())
print()
print("Waiting for connection")
print()

#Functions

#Call to clear the screen between each frame
def cls():
    #cls if on windows, clear if on linux
    os.system('cls' if os.name=='nt' else 'clear')

#Function  to set the title of the terminal
def set_terminal_title(title):
    # Use an escape sequence to set the terminal title

    sys.stdout.write(f"\033]0;{title}\007")
    sys.stdout.flush()


#The main  netcode for reciving the image       
def receive_file_over_socket(filename, port):

    #This "client" is actually a server as it is the reciving side

    #Bind socket to self (0.0.0.0 is used instead of 127.0.0.1 for cross platform connectivity)
    #Start the connection on our specified port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
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
        
      #  print("File received successfully")






#Wait untill the user presses  enter so  there is no exception of the user  number not existing from the other script
#Also wait to resize the window so the setup process is not confusing for the user
input("Ready?")
#Setup the window at the correct size for the ascii image
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=60, cols=170))
#Set the title
set_terminal_title("Their camera:")


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
                
