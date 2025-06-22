import socket
import threading

# Server IP and port
HOST = input("Enter server IP: ")  # e.g., 192.168.1.10
PORT = 4444

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        msg = f'{nickname}: {input("")}'
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
