#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP

# jiarong: get all interfaces and select the eth0
def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv)<3:
        print 'pass 2 arguments: <destination> "<message>"'
        exit(1)

    # jiarong: get the ip address of the host, can be set manually
    addr = socket.gethostbyname(sys.argv[1])
    # jiarong: can be set manually 
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
	# jiarong: create a packet    
	pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / sys.argv[2]
	# jiarong: print the packet    
	pkt.show2()
	# jiarong: send it out
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
