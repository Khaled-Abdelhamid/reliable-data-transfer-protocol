import os
import math
import socket

packet_size = 512
dest_ip = '192.168.1.11'
dest_port = '1234'
socket_timeout = 1
pkt_timeout = 1
window_size = 10
payload_size = 5


class Sender:
    def __init__(self, dest_ip, dest_port, socket_timeout, pkt_timeout, window_size, payload_size):
        self.sock = 1
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.socket_timeout = socket_timeout
        self.pkt_timeout = pkt_timeout
        self.window_size = window_size
        self.payload_size = payload_size

    def send_file(self, fname):
        try:
            f = open(fname, 'rb')
            self.make_packets(fname)
        except IOError:
            print(fname, 'not found!')

    def make_packets(self, fname):
        file_size = os.path.getsize(fname)
        num_packets = math.ceil(file_size / self.payload_size) + 1
        seq_num_bytes = math.ceil(num_packets.bit_length() / 8)
        f = open(fname, 'rb')
        packets = []
        for i in range(num_packets):
            packets.append(i.to_bytes(
                seq_num_bytes, byteorder='little', signed=False) + b'\r\n' + f.read(payload_size))
        self.packets = packets

    def send_pkt(self, pkt):
        pass

    def resv_ack(self):
        pass


if __name__ == "__main__":
    sender = Sender(dest_ip, dest_port, socket_timeout,
                    pkt_timeout, window_size, payload_size)

    sender.make_packets('test.txt')
