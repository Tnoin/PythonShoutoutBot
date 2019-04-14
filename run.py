import string
import re
import sys

from read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from settings import SHOUTOUT, LEAVEMESSAGE, IDENT


s = openSocket()
joinRoom(s)
readbuffer = ""
shouted = dict()
for user in SHOUTOUT:#prepare the list of potential shoutouts
	shouted[user] = False
	
while True:
	readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()

	for line in temp:
		#print(line) #Development output, prints the raw message
		if "PING" in line:#this just keeps the connection allive
			s.send(bytes("PONG tmi.twitch.tv\r\n","UTF-8"))
			#print("we were pinged")
			break
		user = getUser(line)
		message = getMessage(line)
		if user == IDENT:  #if the account owner says something
			if "bye bot" in message.lower():
				sendMessage(s, LEAVEMESSAGE)
				sys.exit()
		if user in SHOUTOUT:	
			if(shouted[user]==False):#make sure no two shoutouts
				sendMessage(s, SHOUTOUTMESSAGE+user)
				shouted[user]=True
				

