import string

def getUser(line):
	seperate = line.split(":",2)
	user = seperate[1].split("!",1)[0]
	return user

def getMessage(line):
	seperate = line.split(":",2)
	message = seperate[2]
	return message
