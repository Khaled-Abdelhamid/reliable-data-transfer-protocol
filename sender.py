import socket
import time
import datetime


class Sender:
    def __init__(
        self,
        rcv_ip,
        rcv_port=1234,
        socket_timeout=10,
        timer=0,
        timeout_period=1,
        window_size=10,
    ):
        """[summary]

        Args:
            rcv_ip ([type]): the reciever ip
            rcv_port (int, optional): the reciever port. Defaults to 1234.
            socket_timeout (int, optional): the connection timeout after which the socket closes. Defaults to 10.
            timer (int, optional): a counter that holds the date of the last acknowledgment packet. Defaults to 0.
            timeout_period (int, optional): the period after which all packets in the window are resent. Defaults to 1.
            window_size (int, optional): The size of the windo in the GBN. Defaults to 10.

        """
        self.sock = 1
        self.rcv_ip = rcv_ip
        self.rcv_port = rcv_port
        self.socket_timeout = socket_timeout
        self.timer = timer
        self.timeout_period = timeout_period
        self.window_size = window_size
        self.packets_number = 0
        self.packet_list = []

    def UDPConnect(self):

        # Create a datagram socket
        UDP_sender_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        print("UDP sender up and listening")
        # Send to server using created UDP socket
        file_info = f"0\r\n{self.packets_number}"
        try:
            UDP_sender_socket.sendto(
                file_info.encode("utf_8"), (self.rcv_ip, self.rcv_port)
            )
            UDP_sender_socket.settimeout(2)
            _, addr = UDP_sender_socket.recvfrom(1)
            print("established connection with: ", addr)
            UDP_sender_socket.settimeout(self.socket_timeout)
        except socket.timeout:
            print("reciever didnt respond, connection failed")
            UDP_sender_socket.close()

    def send_file(self, fname):
        send_base = 0
        next_seq_num = 0
        while True:
            if next_seq_num < send_base + self.window_size:
                self.send_pkt(self.packet_list[next_seq_num])
                next_seq_num += 1

    def send_pkt(self, pkt):
        pass

    def resv_ack(self):
        # self.sock.recv()
        pass

    def CheckTimeout(self) -> bool:
        now = datetime.datetime.utcnow()
        if int((now - self.timer).total_seconds()) > self.timeout_period:
            return True
        else:
            return False


if __name__ == "__main__":

    packet_size = 512
    rcv_ip = "192.168.1.10"
    rcv_port = "1234"
    socket_timeout = 10
    timer = 1
    window_size = 10

    sender = Sender(rcv_ip, rcv_port, socket_timeout, timer, window_size)

