import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

host = raw_input("Enter the host name: ")

sport  = input("Enter the port number: ")

s.connect((str(host),int(sport)))

conncted = False

while True:
	if conncted == False:
		message = s.recv(1024)
		if str(message) == "Success":
			conncted = True;
			print "Successfully conncted"
		else :
			continue
	userInput = str(raw_input("Enter command:"))
	command = userInput.split(" ",2)
	if(command[0] == "GET"):
		if(len(command) == 1):
			print "please input file name"
			continue
		filename = command[1]
		#print(filename)
		s.send("GET")
		s.send(filename)
		hasfile = s.recv(1024)
		#print hasfile
		if hasfile[:4] == "True":
			filesize = long(hasfile[4:])
			f = open("new" + filename,'w')
			#print "hasfile"
			totalrecv = 0;
			while totalrecv < filesize:
				l = s.recv(1024)
				totalrecv = totalrecv + len(l)
				f.write(l)
				#print str(l)
				#print "receiving"
			f.close()
			print("Done receiving")
		else:
			print("ERROR:no such file")
	elif command[0] == "BOUNCE":
		if(len(command) > 1):
			s.send(command[0])
			s.send(command[1])
		else:
			print "NO text to command"
	elif command[0] == "EXIT":
		s.send("EXIT")
		if len(command )> 1:
			s.send(command[1])
		s.close()
		break
	else:
		print "please input legal command"


