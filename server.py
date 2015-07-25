__author__ = 'ricky phillip vaughn jr'

from socket import *
import thread


def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr

    while 1:
        data = clientsocket.recv(1024)
        if not data:
            break
        else:
            print clientaddr, data
            inCommand = data.split(",")
            if inCommand[0] == "$settest":
                mylist = data.split(",")
                var1 = mylist[1]
                var2 = mylist[2]
                var3 = mylist[3]
                clientsocket.send("set")
                print "settest: " + var1 + " " + var2 + " " + var3
            elif inCommand[0] == "$gettest":
                clientsocket.send("$test," + var1 + "," + var2 + "," + var3)
                print "test: " + var1 + " " + var2 + " " + var3
            else: clientsocket.send("COMMAND NOT FOUND")
    clientsocket.close()

if __name__ == "__main__":

    host = '192.168.1.142'
    port = 55567
    buf = 1024
    inCommand = 0
    var1 = 0
    var2 = 0
    var3 = 0

    addr = (host, port)

    serversocket = socket(AF_INET, SOCK_STREAM)

    serversocket.bind(addr)

    serversocket.listen(2)

    while 1:
        print "Server is listening for connections\n"

        clientsocket, clientaddr = serversocket.accept()
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    serversocket.close()
