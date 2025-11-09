#sample tcp server

import time
import socket
from constants import HOST, PORT, BUFFER_SIZE, NUM_MESSAGES, SERVER_MESSAGE
import asyncio

BACKLOG = 5

# Coroutine to handle a single client connection
async def handle_client(client_reader, client_writer):
    addr = client_writer.get_extra_info('peername')  # Get client address
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    await asyncio.sleep(3)  # Simulate processing delay
    client_writer.write(SERVER_MESSAGE.encode())  # Send message to client
    await client_writer.drain()  # Ensure data is sent
    data = await client_reader.read(BUFFER_SIZE)  # Read data from client
    print(data.decode())  # Print received data
    client_writer.close()  # Close the connection
    await client_writer.wait_closed()  # Wait until the connection is closed

# Main coroutine to start the server and accept connections
async def main():
    # Create a TCP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse
    server_sock.bind((HOST, PORT))  # Bind socket to address and port
    server_sock.listen(BACKLOG)  # Start listening for connections
    server_sock.setblocking(False)  # Set socket to non-blocking mode
    print(f"Server listening on {HOST}:{PORT}")

    loop = asyncio.get_running_loop()  # Get the current event loop
    try:
        while True:
            # Accept a new client connection asynchronously
            client_sock, addr = await loop.sock_accept(server_sock)
            client_sock.setblocking(False)  # Set client socket to non-blocking
            # Wrap the socket with asyncio streams
            client_reader, client_writer = await asyncio.open_connection(sock=client_sock)
            # Handle the client in a separate task
            asyncio.create_task(handle_client(client_reader, client_writer))
    except KeyboardInterrupt:
        print("Server shutting down.")  # Handle Ctrl+C gracefully
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other errors
    finally:
        server_sock.close()  # Ensure the server socket is closed

# Run the main coroutine
asyncio.run(main())