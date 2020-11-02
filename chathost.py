import socket
import threading

HOST = '127.0.0.1' 
PORT = 5060
DISCONNECT = "q!"
CONNECTED_CLIENTS = []
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

def handle_client(conn, addr):
    print(f"NEW CONENCTION {addr} connected.")
    while True:
        try:
            data = conn.recv(2048)
            if data:
                print(f"{addr}{data}")
                send_message(data,addr+":\t",conn)
                if data == bytes(DISCONNECT, FORMAT):
                    CONNECTED_CLIENTS.remove(conn)
                    conn.close()
                    print(f"{addr} Disconnected.")
                    print(f"ACTIVE CONNECTIONS {len(CONNECTED_CLIENTS)}")
            else:
                if conn in CONNECTED_CLIENTS:
                    CONNECTED_CLIENTS.remove(conn)
                    break
        except:
            break

def send_message(msg,addr,conn):
    for client in CONNECTED_CLIENTS:
        client.send(bytes(addr, FORMAT) + msg)
        if client not in CONNECTED_CLIENTS:
            conn.close()
            CONNECTED_CLIENTS.remove(client)

def start():
    s.listen()
    print(f"Server running on {HOST}")
    while True:
        conn, addr = s.accept()
        CONNECTED_CLIENTS.append(conn)
        thread = threading.Thread(target = handle_client, args=(conn,addr[0]))
        thread.start()
        print(f"ACTIVE CONNECTIONS {len(CONNECTED_CLIENTS)}")


start()
s.close()
