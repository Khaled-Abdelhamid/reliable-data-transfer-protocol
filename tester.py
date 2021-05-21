import os
import math


def make_packets(fname, payload_size):
    file_size = os.path.getsize(fname)
    num_packets = math.ceil(file_size / payload_size) + 1
    seq_num_bytes = math.ceil(num_packets.bit_length() / 8)
    f = open(fname, 'rb')
    packets = []
    for i in range(num_packets):
        packets.append(i.to_bytes(
            seq_num_bytes, byteorder='little', signed=False) + b'\r\n' + f.read(payload_size))
    return packets


print(make_packets('test.txt', 4))
