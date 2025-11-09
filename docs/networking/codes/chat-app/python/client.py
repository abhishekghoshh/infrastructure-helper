import socket
import uuid
from constants import HOST, PORT, BUFFER_SIZE
import threading
import asyncio
import sys

async def chat(client_socket, client_name):
    connection_closed = threading.Event()

    def receive_messages(sock):
        print("Receiving messages from the server...")
        while True:
            try:
                response = sock.recv(BUFFER_SIZE)
                if not response:
                    print("\nServer closed the connection.")
                    connection_closed.set()
                    break
                print(f"\rServer: {response.decode()}\nYou: ", end='', flush=True)
            except Exception as e:
                print(f"\nError receiving message: {e}")
                connection_closed.set()
                break

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    print("Type your message and press Enter to send. Type 'exit' to quit.")

    while not connection_closed.is_set():
        try:
            # Wait for input only if connection is not closed
            if connection_closed.is_set():
                break
            try:
                message = input("You: ")
            except (KeyboardInterrupt, EOFError):
                break
            if connection_closed.is_set():
                break
        except EOFError:
            break
        if message.lower() == 'exit':
            print("Closing connection.")
            break
        elif not message.strip():
            continue
        else:
            try:
                client_socket.send(message.encode())
            except Exception:
                print("Failed to send message. Connection may be closed.")
                break

    # Graceful shutdown
    connection_closed.set()
    try:
        client_socket.shutdown(socket.SHUT_RDWR)
    except Exception:
        pass
    client_socket.close()
    print("Disconnected from server.")
    sys.exit(0)  # Ensure exit with code 0

async def main():
    client_socket = None
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_id = uuid.uuid4()
        print(f"Client ID: {client_id}")
        print(f"Connecting to server at {HOST}:{PORT}...")
        print("Sending message to server...")
        client_socket.send(str(client_id).encode())
        client_name = client_socket.recv(BUFFER_SIZE)
        print("Client Name:", client_name.decode())
        await chat(client_socket, client_name)
    except ConnectionRefusedError:
        print(f"Connection refused: Unable to connect to the server at {HOST}:{PORT}")
    except socket.timeout:
        print("Connection timed out: The server did not respond in time.")
    except socket.error as e:
        print(f"Socket error: {e}") 
    except ConnectionResetError:
        print(f"Connection reset by peer: The server closed the connection unexpectedly.")
    except ConnectionAbortedError:
        print(f"Connection aborted: The connection was closed by the server.")  
    except socket.gaierror:
        print(f"Address-related error connecting to server at {HOST}:{PORT}")
    except socket.herror:
        print(f"Hostname error: Unable to resolve the host {HOST}")
    except TimeoutError:
        print("Timeout error: The operation timed out.")
    except KeyboardInterrupt:
        print("Client interrupted by user.")
    except Exception as error:
        print(f"An error occurred: {error}")
    finally:
        if client_socket:
            try:
                client_socket.close()
            except Exception:
                pass
        sys.exit(0)  # Ensure exit with code 0

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Client interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(0)
