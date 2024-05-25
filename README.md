# Ascii-webcam

This program functions as a  (non-practical) video confrencing program with a unique twist. Video is displayed through text and ascii characters instead of images, meaning the program can run completely in the command line. As there is no way to transmit audio directly over text the program detects user speech and displays it as text.


There is both a windows and linux version avalible.  They  are cross-platform, but the linux version does not suppourt speech detection 

The program requires python 3.12 as well as the following pip packages

Numpy

Pillow

opencv-python

SpeechRecognition

pyttsx3

These can be installed by running script included with the program, or downloaded manually. 

# Running the program

Make sure that the two scripts stay in the same directory as they both need to refrence one of the same files for operation. 

To run the program, have both users run their server and client scripts at the same time.

Each users ip address will be  displayed on their client, and should be input on the oposite server.

Then decide who is user one and who is user two, the user number does not affect operation but the program will not function if both users select the same number.

After that, both users can press enter on their client, and the program will start.






