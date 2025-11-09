#simple udp server

import socket
from time import sleep
from constants import HOST, PORT, BUFFER_SIZE, SERVER_MESSAGE
import asyncio



async def handle_client(server_socket):
    loop = asyncio.get_running_loop()
    while True:
        try:
            client_data, client_addr = await loop.run_in_executor(
                None, server_socket.recvfrom, BUFFER_SIZE
            )
            print("client data received:", client_data.decode('utf-8'), ", from", client_addr)
            asyncio.create_task(process_and_respond(server_socket, client_addr))
        except (OSError, asyncio.CancelledError) as e:
            print(f"Server socket error or cancelled: {e}")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            continue

async def process_and_respond(server_socket, client_addr):
    try:
        await process_client_req(client_addr)
        print("Sending response to client:", SERVER_MESSAGE)
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None, server_socket.sendto, SERVER_MESSAGE.encode('utf-8'), client_addr
        )
    except Exception as e:
        print(f"Error sending response: {e}")

async def process_client_req(client_addr):
    for _ in range(10):
        print("Processing... for client:", client_addr)
        await asyncio.sleep(1)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        server_socket.bind((HOST, PORT))
        asyncio.run(handle_client(server_socket))
    except KeyboardInterrupt:
        print("Server interrupted by user. Shutting down.")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Socket closed.")

if __name__ == "__main__":
    main()
