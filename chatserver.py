import socket
import threading

# Server details
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444       # You can change this port

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast messages to all clients
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            client.send(message)

# Handle client messages
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('utf-8'))
            nicknames.remove(nickname)
            client.close()
            break

# Accept connections
def receive():
    print(f"[SERVER STARTED ON PORT {PORT}]")
    while True:
        client, address = server.accept()
        ip, port = address
        print(f"[NEW CONNECTION] IP: {ip}, Port: {port}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"[NICKNAME SET] {ip}:{port} → {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
