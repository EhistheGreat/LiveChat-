# LiveChat-




## how It Works

- The server listens for incoming TCP connections.
- Each client connects to the server using the same IP and port.
- The server receives messages and broadcasts them to all connected clients.
- Each client can type and receive messages in real time.
- Users are identified by their **IP address** or **name** (if added).

---

## 🚀 Getting Started

### ✅ 1. Start the Server

In one terminal:

```bash
run python3 chatserver.py n host machine 

then aslo run the clientchat.py app on another machine 
you can have 3 or more clients on the server ,and they would be able to communicate well each with indicated user name 

would be like a group chat

this program can only be used locally , for devices connected to your where your chatserver.py runs(server host)

