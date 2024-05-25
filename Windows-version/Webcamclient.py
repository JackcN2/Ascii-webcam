import socket
import time
import os
import ctypes
import sys, random, argparse

hostname = socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your ip is" +IPAddr)
print("Waiting for connection")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def set_cmd_window_size(width, height):
    STD_OUTPUT_HANDLE = -11
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



    
def receive_file_over_socket(filename, port):
    HOST = "0.0.0.0"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen(1)
    
        #print("Waiting for connection...")
        conn, addr = s.accept()
        #print("Connected by", addr)    
        with open(filename, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    #print("recived")
                    break
                file.write(data)
        
      #  print("File received successfully")


set_cmd_window_size(170, 60)
ctypes.windll.kernel32.SetConsoleTitleW('Their camera:')
filename = "camcache.txt"

# Change this to the name you want to save the received file as

#wait untill the user presses  enter so  there is no exception of the user  number not existing from the other script
input("Ready?")
with open('runtimevariables.txt', 'r') as file:
    # Read the first character
    person = file.read(1)
#reverse of our server
if person == "1":
    port = 12344
elif person == "2":
    port = 12345
print(port)
while True:
    
    receive_file_over_socket(filename, port)
    cls()
  
    with open(filename, 'r') as file:
        # Read the lines of the file
        file_lines = file.readlines()
 
        # Print each line
        
        
        for index, line in enumerate(file_lines):
            print(line.strip())
                
