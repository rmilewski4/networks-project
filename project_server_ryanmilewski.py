#CS4850 Networks Project (server)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022


import socket

ipaddr = "127.0.0.1"
port = 17022
#implement checking if file exists
def setupAccount(username, password):
    with open('users.txt') as f:
        if username in f.read():
            return "> Denied. Please login first."
    file = open("users.txt","a+")
    file.write("\n(" + username + ", " + password + ")")
    file.close()
    print("New user account created.\n")
    return "> New user account created. Please login"


def loop():
    print("My chat room server. Version One.\n\n")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ipaddr, port))
    serversocket.listen(5)
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
                print(decodedData)
                dataArr = decodedData.split(' ')
                if dataArr[0] == "login":
                    print()
                elif dataArr[0] == "newuser":
                    returndata = setupAccount(dataArr[1], dataArr[2])
                clientsocket.sendall(bytes(returndata, 'utf-8'))


if __name__ == "__main__":
    loop()