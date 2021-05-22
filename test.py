import math
import os

fname = "dummy_send.txt"
data_size = 50  # in characters
file_size = os.path.getsize(fname)
num_packets = math.ceil(file_size / (data_size * 4))
seq_num_bytes = math.ceil(num_packets.bit_length() / 8)

with open(fname, mode="r", encoding="utf8") as f:
    all_of_it = f.read()  # all data content in a string format
print(all_of_it)
packets = []
for i in range(num_packets):
    packets.append(i + "\r\n" + )
