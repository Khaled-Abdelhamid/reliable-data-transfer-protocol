def read_segments(
    fname,
    MTU=1526,
    Ethernet_header_size=14,
    IP_protocol_header_size=20,
    UDP_protocol_header_size=8,
):
    """ This function is used to read a data file and divides it into segments of packets depending on MSS
        
        input: 
            fname: file name and it is the main input
            
            other inputs are just for real MSS calculations and they are initialized with
            typical values after some search
            
        output:
            packets_list: a list of packets data with its ids (as strings in the required format)
            required format ==>     PackerID \r\n Data
        
    """

    with open(fname, mode="r") as f:

        all_of_it = f.read()  # all data content in a string format

    # This MSS calculation is what actually happens
    MSS = Ethernet_header_size - IP_protocol_header_size - UDP_protocol_header_size
    # but here I am just assuming a value for MSS to test easily
    MSS = 5  # remove this line to use a calculated MSS

    fsize = len(all_of_it)

    one_full_packet = fsize // MSS  # a full packet size (=5 here)
    full_packets = MSS * one_full_packet  # total size of all full packets (=35 here)

    packets_list = []

    chunks = [
        all_of_it[x : x + one_full_packet]
        for x in range(0, full_packets, one_full_packet)
    ]  # list

    if all_of_it[full_packets:fsize] != "":
        chunks.append(
            all_of_it[full_packets:fsize]
        )  # appending the non-complete packet if exists

    for ID, data in enumerate(chunks, 1):
        packets_list.append(str(ID) + "\r\n" + data)

    return packets_list


print(read_segments("dummy_send.txt")[2])
