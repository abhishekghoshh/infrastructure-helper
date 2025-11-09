import socket
from constants import HOST, PORT, BUFFER_SIZE, NUM_MESSAGES, CLIENT_MESSAGE

try:
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    client_socket.connect((HOST, PORT))

    # Receive data from the server
    received_data = client_socket.recv(BUFFER_SIZE)
    print(received_data.decode())

    # Send a single message to the server
    client_socket.send(CLIENT_MESSAGE.encode())

except ConnectionRefusedError:
    # Raised if the server actively refuses the connection
    print(f"Connection refused: Unable to connect to the server at {HOST}:{PORT}")
except socket.timeout:
    # Raised if a timeout occurs on a socket operation
    print("Connection timed out: The server did not respond in time.")
except socket.error as e:
    # Generic socket error
    print(f"Socket error: {e}") 
except ConnectionResetError:
    # Raised if the connection is reset by the peer
    print(f"Connection reset by peer: The server closed the connection unexpectedly.")
except ConnectionAbortedError:
    # Raised if the connection is aborted
    print(f"Connection aborted: The connection was closed by the server.")  
except socket.gaierror:
    # Raised for address-related errors (e.g., invalid hostname)
    print(f"Address-related error connecting to server at {HOST}:{PORT}")
except socket.herror:
    # Raised for errors related to the host
    print(f"Hostname error: Unable to resolve the host {HOST}")
except socket.error as e:
    # Catch-all for other socket errors (duplicate, but included for completeness)
    print(f"Socket error: {e}")
except TimeoutError:
    # Raised if an operation times out
    print("Timeout error: The operation timed out.")
except KeyboardInterrupt:
    # Handle user interruption (Ctrl+C)
    print("Client interrupted by user.")
except Exception as error:
    # Catch-all for any other exceptions
    print(f"An error occurred: {error}")
finally:
    try:
        # Ensure the socket is closed properly
        client_socket.close()
    except Exception:
        # Ignore errors while closing the socket
        pass
