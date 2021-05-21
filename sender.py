import socket

packet_size = 512
dest_ip = '192.168.1.11'
dest_port = '1234'
socket_timeout = 1
pkt_timeout = 1
window_size = 10


class Sender:
    def __init__(self, dest_ip, dest_port, socket_timeout, pkt_timeout, window_size):
        self.sock = 1
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.socket_timeout = socket_timeout
        self.pkt_timeout = pkt_timeout
        self.window_size = window_size

    def send_file(self, fname):
        try:
            f = open(fname, 'rb')
        except IOError:
            print(fname, 'not found!')

    def send_pkt(self, pkt):
        pass

    def resv_ack(self):
        # self.sock.recv()
        pass


if __name__ == "__main__":
    sender = Sender(dest_ip, dest_port, socket_timeout,
                    pkt_timeout, window_size)
