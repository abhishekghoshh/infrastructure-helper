#simple udp client

import socket
from constants import HOST, PORT, BUFFER_SIZE, CLIENT_MESSAGE
# Generate a unique client ID


import uuid
client_id = uuid.uuid4()  # Generate a unique client ID

try:
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Client ID: {client_id}")
    # Send message to the server
    sock.sendto(f"from client {client_id}, message : {CLIENT_MESSAGE}".encode('utf-8'), (HOST, PORT))

    # Receive response from the server
    data = sock.recvfrom(BUFFER_SIZE)
    print("Received from server:", data[0].decode('utf-8'))
except socket.error as e:
    # Handle generic socket errors
    print("Socket error:", e)
except ConnectionRefusedError:
    # Handle case when server refuses the connection
    print(f"Connection refused: Unable to connect to the server at {HOST}:{PORT}")
except socket.timeout:
    # Handle timeout if server does not respond
    print("Connection timed out: The server did not respond in time.")
except socket.gaierror:
    # Handle address-related errors
    print(f"Address-related error connecting to server at {HOST}:{PORT}")
except socket.herror:
    # Handle hostname resolution errors
    print(f"Hostname error: Unable to resolve the host {HOST}")
except ConnectionResetError:
    # Handle case when server closes the connection unexpectedly
    print(f"Connection reset by peer: The server closed the connection unexpectedly.")
except ConnectionAbortedError:
    # Handle case when connection is aborted by the server
    print(f"Connection aborted: The connection was closed by the server.")
except TimeoutError:
    # Handle generic timeout errors
    print("Timeout error: The operation timed out.")
except KeyboardInterrupt:
    # Handle user interruption
    print("Client interrupted by user.")
except Exception as e:
    # Handle any other exceptions
    print("An error occurred:", e)
finally:
    # Always close the socket
    sock.close()