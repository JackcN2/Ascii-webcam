# Ascii-webcam

This program functions as a  (non-practical) video confrencing program with a unique twist. Video is displayed through text and ascii characters instead of images, meaning the program can run completely in the command line. As there is no way to transmit audio directly over text the program detects user speech and displays it as text.


There is both a windows and linux version avalible.  They  are cross-platform, but the linux version does not suppourt speech detection 

# Setup

The program requires python 3.12 (or 3.11) as well as the following pip packages

Numpy

Pillow

opencv-python

SpeechRecognition

pyttsx3

requests

These can be installed by running the command script included with the program, or downloaded manually. 

Download the zip from github, unzip it and open the file  for the operating  system you are currently on.
Alternativly you can download the project by cloning  'https://github.com/JackcN2/Ascii-webcam.git'

Make sure that the two python scripts stay in the same directory as they both need to refrence one of the same files for operation. 

# Running the program

See  #Limitations if both computers are not on the  same network

To run the program, have both users run their server and client scripts at the same time.

Each users ip address will be  displayed on their client, and should be input on the oposite server.

Then decide who is user one and who is user two, the user number does not affect operation but the program will not function if both users select the same number.

After that, both users can press enter on their client, and the program will start.

# Using the Program


Your own camera feed is displayed under the window titled "Your camera:" and the other users camera feed is displayed under the window titled "Their camera:"

If you are  running on windows, you can speak into the microphone and it will display what you said above your video feed.


# Limitations

On linux install script will not function unless you chmod its  permissions to make it be executable

Due to the nature of the programs netcode, additional steps by each user is required if  you  want to connect two computers not on the same network.

For the sockets to be pointed to the right address, both users must forward TCP ports 12345 and  12344 to their computers. A  guide for general port forwarding is avalible  here: https://www.noip.com/support/knowledgebase/general-port-forwarding-guide

Once this is completed you can enter the other users external ip instead of their internal one and it should work as normal. 

