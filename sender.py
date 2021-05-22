import os
import math
import socket
import time
import datetime
import threading
import logging

logging.getLogger().setLevel(logging.INFO)


class Sender:
    def __init__(
        self,
        receiver_ip,
        receiver_port,
        filename="",
        socket_timeout=10,
        window_size=10,
        data_size=100,
        timeout_period=2,
    ):
        """[summary]

        Args:
            receiver_ip ([type]): the reciever ip
            receiver_port (int, optional): the reciever port. Defaults to 1234.
            socket_timeout (int, optional): the connection timeout after which the socket closes. Defaults to 10.
            timer (int, optional): a counter that holds the date of the last acknowledgment packet. Defaults to 0.
            timeout_period (int, optional): the period after which all packets in the window are resent. Defaults to 1.
            window_size (int, optional): The size of the windo in the GBN. Defaults to 10.

        """
        self.receiver_ip = receiver_ip
        self.receiver_port = receiver_port
        self.filename = filename
        self.receiver_address = (receiver_ip, receiver_port)
        self.socket_timeout = socket_timeout
        self.timeout_period = timeout_period
        self.timer = timer
        self.window_size = window_size
        self.data_size = data_size
        self.packets_number = 0
        self.lastACK = None
        self.packets = []

        self.UDPConnect()
        self.makePackets(self.filename)
        t1 = threading.Thread(target=self.receiveAck)
        t2 = threading.Thread(target=self.sendFile)
        t1.start()
        t2.start()

    def UDPConnect(self):

        # Create a datagram socket
        self.UDP_sender_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM
        )
        # Send to server using created UDP socket
        file_info = f"0\r\n{self.packets_number}"
        try:
            self.UDP_sender_socket.sendto(
                file_info.encode("utf_8"), self.receiver_address
            )
            self.UDP_sender_socket.settimeout(2)
            _, addr = self.UDP_sender_socket.recvfrom(1)
            logging.info("established connection with: ", addr)
            self.UDP_sender_socket.settimeout(self.socket_timeout)
            self.UDP_sender_socket.bind(self.receiver_address)

        except socket.timeout:
            logging.info("reciever didnt respond, connection failed")
            self.UDP_sender_socket.close()

    def sendFile(self, fname):
        send_base = 0
        next_seq_num = 0
        self.ResetTimer()
        while True:
            if next_seq_num < send_base + self.window_size:
                self.sendPacket(self.packets[next_seq_num])
                next_seq_num += 1

            if self.lastACK > send_base:
                send_base = self.lastACK + 1
                self.resetTimer()

            if self.CheckTimeout():
                self.ResetTimer()
                for pckt in range(send_base, next_seq_num):
                    self.sendPacket(self.packets[pckt])

    def makePackets(self, fname):
        file_size = os.path.getsize(fname)
        num_packets = math.ceil(file_size / self.data_size)
        seq_num_bytes = math.ceil(num_packets.bit_length() / 8)
        f = open(fname, "rb")
        packets = []
        for i in range(num_packets):
            packets.append(
                i.to_bytes(seq_num_bytes, byteorder="little", signed=False)
                + b"\r\n"
                + f.read(self.data_size)
            )
        self.packets = packets
        self.packets_number = len(packets)

    def sendPacket(self, pkt):
        self.UDP_sender_socket.sendto(pkt.encode("utf_8"), self.receiver_address)

    def receiveAck(self):
        # Accept data
        while True:
            message, clientAddress = self.UDP_sender_sockets.recvfrom(1024)
            self.lastACK = message.decode("utf-8")
            return message.decode("utf-8")

    def CheckTimeout(self) -> bool:
        now = datetime.datetime.utcnow()
        if int((now - self.timer).total_seconds()) > self.timeout_period:
            return True
        else:
            return False

    def ResetTimer(self):
        self.timer = datetime.datetime.utcnow()


if __name__ == "__main__":

    packet_size = 512
    receiver_ip = "192.168.1.11"
    receiver_port = "1234"
    socket_timeout = 10
    timer = 1
    window_size = 10
    timeout_period = 2
    filename = ""
    data_size = 100

    sender = Sender(
        receiver_ip=receiver_ip,
        receiver_port=receiver_port,
        filename=filename,
        socket_timeout=socket_timeout,
        window_size=window_size,
        data_size=data_size,
        timeout_period=timeout_period,
    )

