#CS4850 Networks Project (server)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022


import socket
import sys
ipaddr = "127.0.0.1"
port = 17022


def loginUser(username, password):
    file = open("users.txt","a+")
    file.close()
    with open('users.txt') as fp:
        for line in fp:
            split = []
            data = line.strip()
            data = data.replace("(", "")
            data = data.replace(")","")
            data = data.replace(",", "")
            split = data.split(" ")
            if split[0] == username and split[1] == password:
                print(username + "login.")
                return "> login confirmed."
    return "> Denied. User name or password incorrect"

def setupAccount(username, password):
    #opening with a+ will cause the file to be created if it does not exist.
    file = open("users.txt","a+")
    file.close()
    with open('users.txt') as f:
        if username in f.read():
            return "> Denied. User account already exists."
    file = open("users.txt","a+")
    file.write("\n(" + username + ", " + password + ")")
    file.close()
    print("New user account created.\n")
    return "> New user account created. Please login"


def loop():
    print("My chat room server. Version One.\n\n")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind((ipaddr, port))
        serversocket.listen(5)
    except socket.error as error:
        print("Error on active socket: ",error)
        clientsocket.close()
        sys.exit()
    while True:
        print("waiting for connections")
        (clientsocket, address) = serversocket.accept()
        with clientsocket:
            print(f"Connected by {address}")
            while True:
                dataRecv = clientsocket.recv(1024)
                if not dataRecv:
                    break
                decodedData = dataRecv.decode()
                dataArr = decodedData.split(' ')
                if dataArr[0] == "login":
                    returndata = loginUser(dataArr[1], dataArr[2])
                elif dataArr[0] == "newuser":
                    returndata = setupAccount(dataArr[1], dataArr[2])
                elif dataArr[0] == "send":
                    msgArr = (dataArr[2:])
                    message = " ".join(msgArr)
                    returndata = "> " + dataArr[1] + ": " + message
                    print(returndata)
                elif dataArr[0] == "logout":
                    returndata = "> " + dataArr[1] + " left."
                    print(dataArr[1] + " logout.")
                clientsocket.sendall(bytes(returndata, 'utf-8'))


if __name__ == "__main__":
    loop()