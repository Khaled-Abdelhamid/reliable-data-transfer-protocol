import sys
import time
from statistics import mean
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 1  # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientSocket.settimeout(timeout)
# Command line argument is a string, change the port into integer
port = int(port)
# Sequence number of the ping message
ptime = 0
rtime = 0
RTT = []
# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent
    data = "Ping " + str(ptime) + " " + time.asctime()

    try:
        # Sent time
        RTTb = time.time()
        # Send the UDP packet with the ping message
        clientSocket.sendto(data.encode(), (host, port))
        # Receive the server response
        message, address = clientSocket.recvfrom(1024)
        # Received time
        RTTa = time.time()
        # Display the server response as an output
        print("Reply from " + address[0] + ": " + message.decode())
        # Round trip time is the difference between sent and received time
        print("RTT: " + str(RTTa - RTTb))
        rtime += 1
        RTT.append(RTTa-RTTb)
    except OSError:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        continue
print("Statistics")
print("Average RTT: ", mean(RTT))
print("Maximum RTT: ", max(RTT))
print("Minimum RTT: ", min(RTT))
print("Packet loss: ", round((1-rtime/ptime)*100, 2), "%")
# Close the client socket
clientSocket.close()
