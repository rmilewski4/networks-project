#CS4850 Networks Project (server)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022


import socket

ipaddr = "127.0.0.1"
port = 17022

def setupAccount(username, password):
    print(username + password)
    file = open("users.txt","w")


def loop():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ipaddr, port))
    serversocket.listen(5)
    while True:
        print("waiting for connections")
        (clientsocket, address) = serversocket.accept()
        dataRecv = serversocket.recv(1024)
        #dataArr = dataRecv.split(' ')
        #if dataArr[0] == "login":
        #    print()
        #elif dataArr[0] == "newuser":
        #    setupAccount(dataArr[1], dataArr[2])
        #serversocket.close()


if __name__ == "__main__":
    loop()