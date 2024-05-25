import socket
import time
import os
import ctypes
import sys, random, argparse

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

print("Your ip is" +get_ip())
print("Waiting for connection")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def set_terminal_title(title):
    # Use an escape sequence to set the terminal title

    sys.stdout.write(f"\033]0;{title}\007")
    sys.stdout.flush()


    
def receive_file_over_socket(filename, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen(1)
      #  print("Waiting for connection...")
        conn, addr = s.accept()
       # print("Connected by", addr)    
        with open(filename, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
        
      #  print("File received successfully")


sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=60, cols=170))
set_terminal_title("Their camera:")

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

while True:
    
    receive_file_over_socket(filename, port)
    cls()
    with open(filename, 'r') as file:
        # Read the lines of the file
        file_lines = file.readlines()
 
        # Print each line
        
        
        for index, line in enumerate(file_lines):
            
            if index == 2:  # Check if it's the third line
                
                spaced = str(line.strip())
                whitespace = " " * 85
                text_with_whitespace = whitespace + spaced
                print(text_with_whitespace)
            else:
                print(line.strip())
                
