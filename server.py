import socket
import os

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname();

print(host)



port = 9999

sport = input("Enter the port number: ")

port = int(sport)

serversocket.bind((host,port))

serversocket.listen(1)

print "start server"
while True:
    clientsocket, addr = serversocket.accept()
    clientsocket.send("Success")
    print("Got a connection from %s" % str(addr))
    #currentTime = time.ctime(time.time()) + "\r\n"
    while True:
        command = clientsocket.recv(1024)
        #print command
        if(command == "GET"):
            filename = clientsocket.recv(1024)
            try:
                f = open(filename,'r')
            except IOError as e:
                clientsocket.send("False")
            else:
                clientsocket.send("True" + str(os.path.getsize(filename)))
                l = f.read(1024)
                while l:
                    #print("Sending")
                    print l
                    clientsocket.send(l)
                    l = f.read(1024)
                #clientsocket.shutdown(socket.SHUT_WR)
                f.close()
                print("Done sending")
        #clientsocket.send(currentTime.encode('ascii'))
        elif command == "BOUNCE":
            text = clientsocket.recv(1024)
            print text;
        elif command == "EXIT":
            exitCode = clientsocket.recv(1024)
            print "EXIT " + exitCode
            clientsocket.close()
            break
