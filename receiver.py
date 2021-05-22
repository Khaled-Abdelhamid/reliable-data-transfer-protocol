import os
import math
import socket
import time
import datetime
import threading
import logging

logging.getLogger().setLevel(logging.INFO)


class Receiver:
    def __init__(
        self,
        sender_ip,
        sender_port,
        socket_timeout=10,
        window_size=10,
        data_size=100,
        timeout_period=2,
    ):
        """[summary]

        Args:
            sender_ip ([type]): the reciever ip
            sender_port (int, optional): the reciever port. Defaults to 1234.
            socket_timeout (int, optional): the connection timeout after which the socket closes. Defaults to 10.
            timer (int, optional): a counter that holds the date of the last acknowledgment packet. Defaults to 0.
            timeout_period (int, optional): the period after which all packets in the window are resent. Defaults to 1.
            window_size (int, optional): The size of the windo in the GBN. Defaults to 10.

        """
        self.sender_ip = sender_ip
        self.sender_port = sender_port
        self.filename = filename
        self.sender_address = (sender_ip, sender_port)
        self.socket_timeout = socket_timeout
        self.timeout_period = timeout_period
        self.timer = timer
        self.window_size = window_size
        self.data_size = data_size
        self.packets_number = 0
        self.seq_num = 0
        self.packets = []

        self.UDPConnect()

    def UDPConnect(self):

        # Create a datagram socket
        self.UDP_reciever_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM
        )
        # Send to server using created UDP socket
        try:
            self.UDP_reciever_socket.bind(self.sender_address)
            logging.info("The server is ready to receive")
            self.UDP_reciever_socket.settimeout(self.socket_timeout)
            message, clientAddress = self.UDP_reciever_socket.recvfrom(1024)
            _, self.packets_number = self.parsePacket(message.decode("utf-8"))
            # ? should there be 4 ports ? two for sender and two for reciever ?
        except socket.timeout:
            logging.info("reciever didnt respond, connection failed")
            self.UDP_reciever_socket.close()

    def recievePackets(self):
        self.recievePackets()
        self.saveFile()

    def recievePackets(self):
        expected_seq_num = 0
        while True:
            message, clientAddress = self.UDP_reciever_socket.recvfrom(1024)
            self.seq_num, payload = self.parsePacket(message.decode("utf-8"))
            if self.seq_num == expected_seq_num:
                self.savePayload(payload)
                self.sendAck(expected_seq_num)
                expected_seq_num += 1
                if self.seq_num == self.packets_number - 1:
                    break
            else:
                self.sendAck(expected_seq_num - 1)

            self.printprogressBar()

    def parsePacket(self, pkt):
        pass
        # TODO split the recieved message into data and sequence number and put each one in the appropriate class value

    def savePayload(payload):
        pass
        # TODO saves the payloads acknowledged to handle them once the file is finished

    def sendAck(self, seq_num):
        #! fix the ports issue
        pass

    def saveFile(self):
        pass
        # TODO takes all the saved payloads and compile them in file

    def printprogressBar(self):
        progress = self.seq_num / self.packets_number
        print(
            f"({progress*100}) "
            + int(progress * 40) * "="
            + int((1 - progress) * 40 * " ")
        )


if __name__ == "__main__":

    packet_size = 512
    sender_ip = "192.168.1.11"
    sender_port = "4321"
    socket_timeout = 10
    timer = 1
    window_size = 10
    timeout_period = 2
    filename = ""
    data_size = 100

    sender = Receiver(
        sender_ip=sender_ip,
        sender_port=sender_port,
        filename=filename,
        socket_timeout=socket_timeout,
        window_size=window_size,
        data_size=data_size,
        timeout_period=timeout_period,
    )

