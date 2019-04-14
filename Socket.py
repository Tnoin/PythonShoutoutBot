import socket
import time
from settings import HOST, PORT, IDENT, CHANNEL
from oauth import PASS

def openSocket():

	s = socket.socket()
	s.connect((HOST, PORT))	
	s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
	s.send(bytes("NICK " + IDENT + "\r\n", "UTF-8"))
	s.send(bytes("JOIN #" + CHANNEL +"\r\n", "UTF-8"))
	return s

def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(bytes(messageTemp + "\r\n", "UTF-8"))
	print("Sent: " + messageTemp)
