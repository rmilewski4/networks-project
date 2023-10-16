#CS4850 Networks Project (client)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022

#just need to implement error checking throughout the project and add comments

import socket
import sys

ipaddr = "127.0.0.1"
port = 17022
loginStatus = False
username = ""

try:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ipaddr,port))
except:
    print("Client Socket couldn't be opened! Try again!")
    sys.exit()


def sendToServer(data):
    try:
        clientsocket.sendall(bytes(data, 'utf-8'))
    except socket.error as error:
        print("Error on active socket: ", error)
        clientsocket.close()
        sys.exit()

def receiveFromServer():
    try:
        dataRecv = clientsocket.recv(1024)
        dataDecoded  = dataRecv.decode()
        print(dataDecoded)
        return dataDecoded
    except socket.error as error:
        print("Error on active socket: ", error)
        clientsocket.close()
        sys.exit()



def logout():
    global username, loginStatus
    if not loginStatus:
        print("You must first login to logout.")
        return
    dataSend = "logout " + username
    sendToServer(dataSend)
    receiveFromServer()
    clientsocket.close()
    username = ""
    loginStatus = False
    sys.exit()
    

def send(message):
    if not loginStatus:
        print("> Denied. Please login first.")
        return
    if len(message) > 256 or len(message) < 1:
        print("Message should be between 1 and 256 characters")
        return
    dataSend = "send " + username + " " + message
    sendToServer(dataSend)
    receiveFromServer()

def login(splitInput):
    global loginStatus, username
    if loginStatus:
        print("Please logout first before trying to login")
        return
    if len(splitInput[1]) > 32 or len(splitInput[1]) < 3:
        print("Username should be between 3 and 32 characters")
        return
    if len(splitInput[2]) < 4 or len(splitInput[2]) > 8:
        print("Password should be between 4 and 8 characters")
        return
    dataSend = splitInput[0] + " " + splitInput[1] + " " + splitInput[2]
    sendToServer(dataSend)
    dataRecvDecoded = receiveFromServer()
    if "confirmed" in dataRecvDecoded:
        loginStatus = True
        username = splitInput[1]

def newuser(splitInput):
    if loginStatus:
        print("Please logout first before creating a new user.")
        return
    if len(splitInput[1]) > 32 or len(splitInput[1]) < 3:
        print("Username should be between 3 and 32 characters")
        return
    if len(splitInput[2]) < 4 or len(splitInput[2]) > 8:
        print("Password should be between 4 and 8 characters")
        return
    dataSend = splitInput[0] + " " + splitInput[1] + " " + splitInput[2]
    sendToServer(dataSend)
    receiveFromServer()


def loop():
    print("My chat room client. Version One.\n\n")
    while True:
        initInput = input(">")
        splitInput = initInput.split(' ')
        splitInput[0] = splitInput[0].lower()
        if splitInput[0] == "login" and len(splitInput) == 3:
            login(splitInput)
        elif splitInput[0] == "newuser" and len(splitInput) == 3:
            newuser(splitInput)
        elif splitInput[0] == "send":
            msgArr = (splitInput[1:])
            message = " ".join(msgArr)
            send(message)
        elif splitInput[0] == "logout" and len(splitInput) == 1:
            logout()
        else:
            print("Invalid input detected!")


if __name__ == "__main__":
    loop()