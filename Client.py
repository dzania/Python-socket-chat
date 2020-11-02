import socket
import threading

while True:
    try:
        HOST = str(input("Enter ip used by server:\t"))
        PORT = int(input("Enter port number used by server:\t"))
        break
    except:
        ("Error occured try again")

FORMAT = 'utf-8'
DISCONNECT = "q!"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def send_msg():
    print("Welcome to chat server!\nIf you want to quit type 'q!'")
    while True: 
        send_msg = str(input("Enter message:\t"))
        if send_msg:
            send_msg = send_msg.encode(FORMAT)
            s.send(send_msg)
            if send_msg == bytes(DISCONNECT, FORMAT):
                print("You've disconnected from chat")
                s.close()
                break



def recv_msg():
    try:
        while True:
            msg = s.recv(2048).decode(FORMAT)
            print("\n"+msg)
            if not msg:
                print('\nERROR')
                break
    except(OSError):
        pass




t_recieve = threading.Thread(target=recv_msg)
t_recieve.start()

send_msg()
