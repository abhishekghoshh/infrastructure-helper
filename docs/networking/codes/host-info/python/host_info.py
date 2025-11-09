import socket
import sys

def get_local_host_info():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = '127.0.0.1'
    print(f"Hostname: {hostname}")
    print("If internet is on, it will show the actual IP address; otherwise, it will show the loopback address.")
    print(f"IP Address: {ip_address}")

def get_remote_host_info():
    remote_hostname = input("Enter remote hostname: ")
    try:
        remote_ip = socket.gethostbyname(remote_hostname)
        print(f"IP Address of remote host: {remote_ip}")
    except socket.error as err_msg:
        print(f"Error: {err_msg}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python host_info.py [--self|--internet]")
        sys.exit(1)
    arg = sys.argv[1].lower()
    if arg == "--self":
        get_local_host_info()
    elif arg == "--internet":
        get_remote_host_info()
    else:
        print("Invalid argument. Use '--self' or '--internet'.")