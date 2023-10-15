#CS4850 Networks Project (client)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022

import socket

ipaddr = "127.0.0.1"
port = 17022
loginStatus = False
username = ""
#still have to implement overall keeping one connection open. Not continuing to open/close it and finish logout function
def logout():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if loginStatus:
        print("You must first login to logout.")
        return
    

def send(message):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if not loginStatus:
        print("> Denied. Please login first.")
        return
    if len(message) > 256 or len(message) < 1:
        print("Message should be between 1 and 256 characters")
        return
    clientsocket.connect((ipaddr, port))
    dataSend = "send " + username + " " + message
    clientsocket.sendall(bytes(dataSend, 'utf-8'))
    dataRecv = clientsocket.recv(1024)
    clientsocket.close()
    print(dataRecv.decode())

def login(splitInput):
    if loginStatus:
        print("Please logout first before trying to login")
        return
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(splitInput[1]) > 32 or len(splitInput[1]) < 3:
        print("Username should be between 3 and 32 characters")
        return
    if len(splitInput[2]) < 4 or len(splitInput[2]) > 8:
        print("Password should be between 4 and 8 characters")
        return
    clientsocket.connect((ipaddr,port))
    dataSend = splitInput[0] + " " + splitInput[1] + " " + splitInput[2]
    clientsocket.sendall(bytes(dataSend, 'utf-8'))
    dataRecv = clientsocket.recv(1024)
    clientsocket.close()
    dataRecvDecoded = dataRecv.decode()
    print(dataRecvDecoded)
    if "confirmed" in dataRecvDecoded:
        global loginStatus
        loginStatus = True
        global username
        username = splitInput[1]

def newuser(splitInput):
    if loginStatus:
        print("Please logout first before creating a new user.")
        return
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(splitInput[1]) > 32 or len(splitInput[1]) < 3:
        print("Username should be between 3 and 32 characters")
        return
    if len(splitInput[2]) < 4 or len(splitInput[2]) > 8:
        print("Password should be between 4 and 8 characters")
        return
    clientsocket.connect((ipaddr,port))
    dataSend = splitInput[0] + " " + splitInput[1] + " " + splitInput[2]
    clientsocket.sendall(bytes(dataSend, 'utf-8'))
    dataRecv = clientsocket.recv(1024)
    print(dataRecv.decode())
    clientsocket.close()


def loop():
    print("My chat room client. Version One.\n\n")
    while True:
        initInput = input(">")
        splitInput = initInput.split(' ')
        splitInput[0] = splitInput[0].lower()
        print(len(splitInput))
        if splitInput[0] == "login" and len(splitInput) == 3:
            login(splitInput)
        elif splitInput[0] == "newuser" and len(splitInput) == 3:
            newuser(splitInput)
        elif splitInput[0] == "send" and len(splitInput) == 2:
            send(splitInput[1])
        else:
            print("Invalid input detected!")


if __name__ == "__main__":
    loop()