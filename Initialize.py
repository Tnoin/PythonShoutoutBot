import string
from Socket import sendMessage

def joinRoom(s):
	readbuffer = ""
	Loading = True
	print("trying to join chat")
	while Loading:
		readbuffer = s.recv(2048).decode("UTF-8").strip('\n\r')
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
			
					
	sendMessage(s, "Successfully joined chat")
def loadingComplete(line):
	#if('End of /NAMES list' in line):
	if('tnoin = #tnoin :tnoin' in line):
		return False
	else: 
		return True

