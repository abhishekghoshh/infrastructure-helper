
## Make a script which will accpet three flags from the command line: --server, --clients, -- send(client_id, message)
import argparse
import socket
import time
import time
import socket
from constants import HOST, PORT, BUFFER_SIZE, SERVER_MESSAGE
import asyncio
import os

BACKLOG = 5

async def _list_clients(clients, client_writer):
    client_writer.write(len(clients).to_bytes(4, 'big'))  # Send number of clients
    await client_writer.drain() 
    for client_id, client_info in clients.items():
        response = f"Client ID: {client_id}, Name: {client_info['name']}"
        response = str(response).encode()
        client_writer.write(response)
        await client_writer.drain()
        await asyncio.sleep(0.1)  # Sleep to avoid overwhelming the client with messages
    client_writer.close()
    await client_writer.wait_closed()
    print("Sent list of clients to the requesting client.")

# Coroutine to send a message to a specific client
async def _send_message(clients, client_reader, client_writer):
    print("Sending message to a specific client...")
    try:
        # Read the recipient client ID
        recipient_id_bytes = await client_reader.read(BUFFER_SIZE)
        recipient_id = recipient_id_bytes.decode().strip()
        print("recipient_id:", recipient_id)
        # Read the message
        message_bytes = await client_reader.read(BUFFER_SIZE)
        message = message_bytes.decode().strip()
        if recipient_id in clients and clients[recipient_id]['conn'] is not None:
            recipient_writer = clients[recipient_id]['conn']
            recipient_writer.write(message.encode())
            await recipient_writer.drain()
            client_writer.write(f"Message sent to {recipient_id}".encode())
            await client_writer.drain()
        else:
            client_writer.write(f"Client {recipient_id} not found.".encode())
            await client_writer.drain()
    except Exception as e:
        client_writer.write(f"Error sending message: {e}".encode())
        await client_writer.drain()
    finally:
        client_writer.close()
        await client_writer.wait_closed()

# Coroutine to handle a single client connection
async def handle_client(clients,client_reader, client_writer):
    addr = client_writer.get_extra_info('peername')
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_id = await client_reader.read(BUFFER_SIZE)
    client_id_str = client_id.decode().strip()
    if client_id_str == "list_clients":
        await _list_clients(clients, client_writer)
        return
    if client_id_str == "send_message":
        await _send_message(clients, client_reader, client_writer)
        return  
    print("client id:", client_id_str)
    client_name = f"Client-{int(time.time())}"
    print("client name:", client_name)
    client_writer.write(client_name.encode())
    await client_writer.drain()
    # Store only in-memory reference; to persist across script runs, you need inter-process communication or external storage.
    clients[client_id_str] = {
        'id': client_id_str,
        'name': client_name,
        'conn': client_writer  # You can access client_writer from clients[client_id_str]['conn'] elsewhere
    }
    
    print(f"Client {client_id_str} connected with name {client_name}")
    try:
        while True:
            data = await client_reader.read(BUFFER_SIZE)
            if not data:
                print(f"Client {client_id_str} disconnected.")
                break
            message = data.decode().strip()
            print(f"{client_id_str}: {message}")
            # Optionally, handle incoming messages here
    except Exception as e:
        print(f"Error with client {client_id_str}: {e}")
    finally:
        client_writer.close()
        await client_writer.wait_closed()
        print(f"Connection closed for client {client_id_str}")
        if client_id_str in clients:
            del clients[client_id_str]
        print(f"Cleaned up client {client_id_str}")



# Main coroutine to start the server and accept connections
async def server(clients):
    # Create a TCP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
    server_sock.bind((HOST, PORT))  # Bind socket to address and port
    server_sock.listen(BACKLOG)  # Start listening for connections
    server_sock.setblocking(False)  # Set socket to non-blocking mode
    print(f"Server listening on {HOST}:{PORT}")
    loop = asyncio.get_running_loop()  # Get the current event loop
    stop_event = asyncio.Event()

    def shutdown():
        print("Received shutdown signal. Shutting down server gracefully...")
        stop_event.set()

    for sig in ('SIGINT', 'SIGTERM'):
        try:
            loop.add_signal_handler(getattr(__import__('signal'), sig), shutdown)
        except (AttributeError, NotImplementedError):
            # Signal handlers may not be available on all platforms (e.g., Windows)
            pass

    try:
        while not stop_event.is_set():
            try:
                client_sock, addr = await asyncio.wait_for(loop.sock_accept(server_sock), timeout=1.0)
            except asyncio.TimeoutError:
                continue  # Check stop_event periodically
            client_sock.setblocking(False)  # Set client socket to non-blocking
            # Wrap the socket with asyncio streams
            client_reader, client_writer = await asyncio.open_connection(sock=client_sock)
            # Handle the client in a separate task
            asyncio.create_task(handle_client(clients, client_reader, client_writer))
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other errors
    finally:
        server_sock.close()  # Ensure the server socket is closed
        print("Server socket closed. Goodbye!")


def start_server(clients):
    print("Starting server...")
    asyncio.run(server(clients))

def list_clients():
    clients = []
    # make a connection to the server to get the clients and send list_clients command
    print("Listing clients...")
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((HOST, PORT))
        client_sock.send(b"list_clients")
        client_count_bytes = client_sock.recv(4)
        client_count = int.from_bytes(client_count_bytes, 'big')
        print(f"Number of connected clients: {client_count}")
        if client_count == 0:
            print("No clients connected.")
            client_sock.close()
            return clients
        for i in range(client_count):
            response = client_sock.recv(BUFFER_SIZE)
            if not response:
                break
            message = response.decode().strip()
            print(f"{i + 1}: {message}")
            clients.append(message)
        return clients
    except ConnectionRefusedError:
        print(f"Connection refused: Unable to connect to the server at {HOST}:{PORT}")
    except Exception as e:
        print(f"An error occurred while listing clients: {e}")
    finally:
        client_sock.close()
        return clients

def send_message(client_id, message):
    # make a connection to the server to send a message to a specific client
    print(f"Sending message to client {client_id}...")
    print(f"Message: {message}")
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((HOST, PORT))
        client_sock.sendall(b"send_message")
        time.sleep(0.1)
        client_sock.sendall(client_id.encode())
        time.sleep(0.1)
        client_sock.sendall(message.encode())
        response = client_sock.recv(BUFFER_SIZE)
        print(response.decode())
    except ConnectionRefusedError:
        print(f"Connection refused: Unable to connect to the server at {HOST}:{PORT}")
    except Exception as e:
        print(f"An error occurred while sending message: {e}")
    finally:
        client_sock.close()

def open_sendbox():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            clients = list_clients()
            if not clients:
                print("No clients connected. Cannot send message.")
                input("Press Enter to retry or Ctrl+C to exit...")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            print("Connected clients:")
            for i in range(len(clients)):
                print(f"{i + 1}: {clients[i]}")
            idx = input("Enter the client index to send a message to (or 'q' to quit): ")
            if idx.lower() == 'q':
                print("Exiting sendbox gracefully.")
                break
            elif idx.lower() == '' or idx == "\n":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            if idx.isdigit() and 1 <= int(idx) <= len(clients):
                client_id = clients[int(idx) - 1].split(",")[0].split(":")[1].strip()
                print(f"Selected client ID: {client_id}")
                message = input("Enter the message to send: ")
                send_message(client_id, message)
                input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Invalid selection.")
                input("Press Enter to try again...")
                os.system('cls' if os.name == 'nt' else 'clear')
    except (KeyboardInterrupt, EOFError):
        print("\nSendbox interrupted. Shutting down gracefully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", action="store_true", help="Start the server")
    parser.add_argument("--clients", action="store_true", help="List all connected clients")
    parser.add_argument("--sendbox", action="store_true", help="Open sendbox to send messages to clients")
    parser.add_argument("--send", nargs=2, metavar=("client_id", "message"), help="Send a message to a specific client (requires client_id and message)")
    args = parser.parse_args()

    if args.server:
        start_server(clients={})
    elif args.clients:
        list_clients()
    elif args.send:
        client_id, message = args.send
        client_id = client_id.removeprefix("client_id=").strip()
        message = message.removeprefix("message=").strip()
        send_message(client_id, message)
    elif args.sendbox:
        open_sendbox() 
    else:
        print("Please specify a valid option: --server, --clients, or --send client_id message")
        parser.print_help()
        





