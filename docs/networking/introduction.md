# Introduction

## Prerequisites of Ethical Hacking

To become proficient in ethical hacking, you should have a solid foundation in the following areas:

- **Networking**: Gain a deep understanding of how data is transmitted across networks, including the intricacies of IP addressing, routing, switching, subnetting, and the various protocols that govern communication. This knowledge is essential for identifying potential vulnerabilities, understanding how attacks can spread, and effectively defending networked systems.
- **Learn Linux**: Most penetration testing tools and hacking environments are built for Linux. Mastering the Linux command-line interface, understanding the file system hierarchy, managing permissions, and writing shell scripts are crucial skills. This expertise enables you to automate tasks, customize tools, and operate efficiently in real-world scenarios.
- **Learn Programming (Shell Scripting, Python, JavaScript)**: Programming knowledge empowers you to create custom scripts for automation, analyze and modify exploit code, and understand the logic behind attacks. Shell scripting is vital for automating repetitive tasks in Linux, Python is widely used for developing security tools and exploits, and JavaScript is key for understanding and testing web application vulnerabilities.
- **Use Platforms like TryHackMe, HackTheBox, or OverTheWire**: These online platforms offer interactive labs and real-world scenarios where you can practice ethical hacking in a legal, controlled environment. They provide challenges ranging from beginner to advanced, helping you build practical skills and stay updated with the latest techniques.

## Theory

### IP Address

An **IP address** is a unique numerical label assigned to each device on a network, enabling devices to locate and communicate with each other. There are two main types:

- **Public IP Address**: Assigned by your Internet Service Provider (ISP), this address identifies your network on the global internet. Public IPs are globally unique and allow devices to be accessed from anywhere on the internet, making them critical for hosting services.
- **Private IP Address**: Used within local networks (LANs), these addresses are not routable on the internet and are reserved for internal communication. Common ranges include `192.168.x.x`, `10.x.x.x`, and `172.16.x.x` to `172.31.x.x`. Devices with private IPs rely on NAT to access the internet.

A **LAN (Local Area Network)** connects devices within a limited area, such as a home, office, or campus. **NAT (Network Address Translation)** allows multiple devices on a LAN to share a single public IP address for internet access, translating private IPs to the public IP and vice versa, thus conserving public IP addresses and adding a layer of security.

### OSI and TCP/IP Models

#### OSI Model

The **OSI (Open Systems Interconnection) model** is a seven-layer conceptual framework that standardizes the functions of a communication system. Each layer serves a specific purpose:

1. **Physical Layer**: Handles the physical connection between devices, including cables, switches, and the transmission of raw binary data as electrical or optical signals.
2. **Data Link Layer**: Manages direct node-to-node data transfer, error detection and correction, and organizes data into frames. It uses MAC addresses for local delivery.
3. **Network Layer**: Responsible for logical addressing (IP addresses), routing packets across different networks, and handling fragmentation and reassembly of data.
4. **Transport Layer**: Ensures reliable (TCP) or unreliable (UDP) data transfer, manages flow control, segmentation, and error recovery between end systems.
5. **Session Layer**: Establishes, manages, and terminates sessions or connections between applications, ensuring continuous data exchange.
6. **Presentation Layer**: Translates data between application and network formats, handles encryption, decryption, and data compression to ensure data is readable by the receiving system.
7. **Application Layer**: Closest to the end user, it provides network services to applications, such as web browsers and email clients, using protocols like HTTP, FTP, and SMTP.

#### TCP/IP Model

The **TCP/IP model** is a practical, four-layer model used in real-world networking:

1. **Link Layer**: Combines the OSI's Physical and Data Link layers, handling hardware addressing, framing, and the physical transmission of data over the network medium.
2. **Internet Layer**: Corresponds to the OSI's Network layer, responsible for logical addressing, routing, and forwarding packets using protocols like IP.
3. **Transport Layer**: Manages end-to-end communication, reliability, sequencing, and flow control using protocols such as TCP and UDP.
4. **Application Layer**: Encompasses the OSI's Session, Presentation, and Application layers, providing protocols and services for specific data communications like HTTP, FTP, and DNS.

### MAC Address vs. IP Address

- **MAC Address**: A unique, permanent hardware identifier assigned to a network interface card (NIC) by the manufacturer. Operating at the Data Link Layer, MAC addresses are used for local network communication within a LAN. They are typically written in hexadecimal format (e.g., `00:1A:2B:3C:4D:5E`) and rarely change.
- **IP Address**: A logical, often dynamic address assigned to devices on a network, used for identifying and locating devices at the Network Layer. IP addresses can be static (manually assigned) or dynamic (assigned by DHCP), and are essential for routing data across networks (e.g., `192.168.1.1` for IPv4 or `2001:0db8::1` for IPv6).

### Every Protocol Explained As QUICKLY As Possible!

#### Core Networking Protocols

- **HTTP (HyperText Transfer Protocol)**: The primary protocol for transferring web pages and data on the internet. It defines how clients (browsers) and servers communicate, including request and response formats.
- **HTTPS (HTTP Secure)**: An extension of HTTP that uses SSL/TLS encryption to secure data transmission, protecting sensitive information from interception and tampering.
- **TCP (Transmission Control Protocol)**: Provides reliable, ordered, and error-checked delivery of data between applications. It establishes connections, ensures data integrity, and retransmits lost packets.
- **IP (Internet Protocol)**: Handles addressing and routing of packets across networks, ensuring data reaches the correct destination.
- **DNS (Domain Name System)**: Translates human-readable domain names (like `example.com`) into IP addresses. Attacks like DNS spoofing can redirect users to malicious sites by providing false DNS responses.
- **DHCP (Dynamic Host Configuration Protocol)**: Automatically assigns IP addresses, subnet masks, gateways, and DNS settings to devices on a network, simplifying network management.
- **NAT (Network Address Translation)**: Allows multiple devices on a private network to share a single public IP address, translating internal addresses to the public address for internet communication.
- **VLAN (Virtual LAN)**: Segments a physical network into multiple logical networks, improving security, performance, and management by isolating traffic.
- **ARP (Address Resolution Protocol)**: Resolves IP addresses to MAC addresses within a local network, enabling devices to communicate on the same LAN.
- **ICMP (Internet Control Message Protocol)**: Used for network diagnostics and error reporting, such as with the `ping` command to test connectivity.
- **VOIP (Voice Over IP)**: Enables voice communication and multimedia sessions over IP networks, replacing traditional phone systems.
- **NFC (Near Field Communication)**: Facilitates short-range wireless communication between devices, commonly used for contactless payments and data exchange.

#### Networking Concepts

- **VPN (Virtual Private Network)**: Establishes a secure, encrypted tunnel over an untrusted network (like the internet), protecting data privacy and enabling remote access to private networks.
- **Routers**: Devices that forward data packets between different networks, making routing decisions based on IP addresses and network topology.
- **Switches**: Network devices that connect multiple devices within a LAN, using MAC addresses to forward data only to the intended recipient, improving efficiency and security.
- **Firewall**: Hardware or software that monitors and controls incoming and outgoing network traffic based on predefined security rules, protecting networks from unauthorized access and attacks.
- **OSI Model**: The seven-layer model for understanding and designing network protocols and interactions, aiding in troubleshooting and network design.
- **WAN (Wide Area Network)**: A network that spans large geographic areas, connecting multiple LANs and enabling communication over long distances, such as between cities or countries.
- **MAC (Media Access Control)**: Refers to both the MAC address and the sublayer responsible for controlling how devices access the network medium and avoid collisions.
- **LAN (Local Area Network)**: A network covering a small geographic area, such as a home, office, or building, enabling high-speed communication between connected devices.
- **MPLS (Multiprotocol Label Switching)**: A technique for directing and managing data traffic efficiently across complex networks, improving speed and reliability.
- **SD-WAN (Software-Defined Wide Area Network)**: Uses software to centrally manage and optimize WAN connections, enhancing performance, flexibility, and security.
- **Proxy Server**: Acts as an intermediary between clients and servers, providing services such as content filtering, caching, anonymity, and access control.
- **QoS (Quality of Service)**: Mechanisms that prioritize certain types of network traffic (like voice or video) to ensure consistent performance and minimize latency or packet loss.

#### Cyber Security and Hacking Protocols

- **SSH (Secure Shell)**: Provides secure, encrypted remote login and command execution over unsecured networks, commonly used for server administration.
- **Telnet**: Allows remote login to devices but transmits data, including passwords, in plaintext, making it vulnerable to interception and generally considered insecure.
- **SMB (Server Message Block)**: A protocol for sharing files, printers, and other resources between computers on a network, commonly used in Windows environments.
- **FTP (File Transfer Protocol)**: Used for transferring files between client and server, but lacks encryption, exposing data to potential interception.
- **SFTP (SSH File Transfer Protocol)**: A secure alternative to FTP, using SSH to encrypt file transfers and protect data in transit.
- **RDP (Remote Desktop Protocol)**: Enables remote access to the graphical desktop of a Windows computer, allowing full control over the system from another location.
- **SNMP (Simple Network Management Protocol)**: Used for monitoring, managing, and configuring network devices such as routers, switches, and servers.

#### Email and Authentication Protocols

- **SMTP (Simple Mail Transfer Protocol)**: The standard protocol for sending emails between servers and from clients to servers.
- **IMAP (Internet Message Access Protocol)**: Allows clients to access, manage, and organize email messages stored on a mail server, supporting multiple devices and folders.
- **POP3 (Post Office Protocol 3)**: Downloads emails from the server to the client and typically deletes them from the server, making messages accessible offline.
- **LDAP (Lightweight Directory Access Protocol)**: Used for accessing and managing distributed directory information services, such as user authentication and organizational hierarchies.

### Wireless and Security Protocols

- **WPA2 (Wi-Fi Protected Access 2)**: A widely used security protocol for wireless networks, employing AES encryption to protect data and prevent unauthorized access.
- **WPA3**: The latest Wi-Fi security standard, offering stronger encryption, improved protection against brute-force attacks, and enhanced security for public networks.
- **IPSec (Internet Protocol Security)**: A suite of protocols for securing IP communications by authenticating and encrypting each IP packet, commonly used in VPNs.
- **BGP (Border Gateway Protocol)**: The protocol used to exchange routing information between autonomous systems on the internet, playing a critical role in determining how data is routed globally.

#### Emerging Protocols

- **QUIC (Quick UDP Internet Connections)**: A modern transport layer protocol developed by Google, designed for faster, more secure web traffic by reducing latency and improving connection reliability.
- **MQTT (Message Queuing Telemetry Transport)**: A lightweight messaging protocol optimized for small sensors and mobile devices, ideal for IoT applications due to its low bandwidth and high latency tolerance.

### Inside TCP Packets

A **TCP packet (segment)** contains several fields that ensure reliable communication:

- **Source Port & Destination Port**: Identify the sending and receiving applications, allowing multiple services to run on a single device.
- **Sequence Number & Acknowledgment Number**: Track the order of data and confirm receipt, ensuring data is delivered accurately and in sequence.
- **Flags**: Control bits (such as SYN, ACK, FIN, RST, PSH, URG) that manage the state of the connection, including establishing, maintaining, and terminating sessions.
- **Window Size**: Specifies how much data can be sent before requiring an acknowledgment, enabling flow control and efficient data transfer.
- **Checksum**: Validates the integrity of the header and data, detecting errors during transmission.
- **Urgent Pointer**: Indicates if any part of the data is urgent and should be prioritized.
- **Options (optional)**: Allow for additional parameters, such as specifying the maximum segment size or enabling advanced features.
- **Data Payload**: The actual application data being transmitted.

TCP’s mechanisms provide reliable, ordered, and error-checked delivery of data between applications, making it suitable for most internet communications.

### Inside UDP Packets

A **UDP packet (datagram)** is simpler and designed for speed:

- **Source Port & Destination Port**: Identify the sending and receiving applications.
- **Length**: Specifies the total length of the UDP header and data.
- **Checksum**: Provides error-checking for the header and data, though it is optional in IPv4.
- **Data Payload**: The actual data being transmitted.

UDP is connectionless and does not guarantee delivery, order, or error correction, making it faster and more efficient for applications like streaming and gaming, where speed is prioritized over reliability.

### Inside IP Packet

An **IP packet** contains the following fields:

- **Version**: Indicates whether the packet uses IPv4 or IPv6.
- **Header Length**: Specifies the size of the header.
- **Type of Service**: Defines the priority and handling instructions for the packet.
- **Total Length**: The entire size of the packet, including header and data.
- **Identification, Flags, Fragment Offset**: Used for fragmenting large packets and reassembling them at the destination.
- **Time to Live (TTL)**: Limits the packet’s lifespan, preventing it from circulating indefinitely in the network.
- **Protocol**: Specifies the protocol used in the data portion (e.g., TCP, UDP, ICMP).
- **Header Checksum**: Ensures the integrity of the header.
- **Source IP Address**: The sender’s IP address.
- **Destination IP Address**: The recipient’s IP address.
- **Options (optional)**: Additional settings for advanced features.
- **Data Payload**: The encapsulated data, such as a TCP or UDP segment.

### Hacking Tools

- **Nmap**: A powerful and versatile network scanner used to discover hosts, services, open ports, and vulnerabilities on a network. It supports advanced features like OS detection, scriptable interaction, and network mapping.
- **Wireshark**: A leading network protocol analyzer that captures and inspects packets in real time. It is invaluable for troubleshooting, analyzing network traffic, and investigating security incidents by providing deep visibility into network protocols.
- **Metasploit**: A comprehensive penetration testing framework that enables security professionals to find, exploit, and validate vulnerabilities. It includes a vast library of exploits, payloads, and auxiliary modules for automating attacks and testing defenses.
- **Burp Suite**: An integrated platform for web application security testing, offering tools for scanning, crawling, intercepting, and manipulating HTTP/S traffic to identify and exploit vulnerabilities in web applications.
- **SQL Injection**: Not a tool, but a technique used to exploit vulnerabilities in web applications by injecting malicious SQL queries. This can allow attackers to manipulate databases, extract sensitive data, or bypass authentication mechanisms.

