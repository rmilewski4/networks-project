#CS4850 Networks Project (server)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022


import socket

ipaddr = "127.0.0.1"
port = 17022
#implement checking if file exists
def setupAccount(username, password):
    print(username + password)
    file = open("users.txt","a")


def loop():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((ipaddr, port))
    serversocket.listen(5)
    print("waiting for connections")
    (clientsocket, address) = serversocket.accept()
    with clientsocket:
        print(f"Connected by {address}")
        while True:
            dataRecv = clientsocket.recv(1024)
            decodedData = dataRecv.decode()
            print(decodedData)
            dataArr = decodedData.split(' ')
            if dataArr[0] == "login":
                print()
            elif dataArr[0] == "newuser":
                setupAccount(dataArr[1], dataArr[2])
            #clientsocket.close()


if __name__ == "__main__":
    loop()