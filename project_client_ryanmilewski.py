#CS4850 Networks Project (client)
#Name: Ryan Milewski (rsmbby)
#Date: 09/21/2023
#Student Number: 18217022


import socket

ipaddr = "127.0.0.1"
port = 17022
login = False
def Chat():
    print()


def login(splitInput):
    print(splitInput)

def newuser(splitInput):
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
        else:
            print("Invalid input detected!")


if __name__ == "__main__":
    loop()