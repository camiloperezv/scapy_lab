from scapy.all import *

data = Raw(load='i am the data\n')
ip = '192.168.178.34'
port = 8888
l4 = UDP(dport=port, sport=5000)
l3 = IP(dst=ip)

p3 = l3/l4/data
send(p3)

# arp -a

# get the mac adress resolution protocol
a = ARP(pdst = ip)
rr = sr(a)
mac = rr[0][0][1].hwsrc

l2 = Ether(dst=mac)
p2 = l2/l3/l4/data
sendp(p2)

my_mac = 'ff:c6:3f:21:92:80'
l2.src = my_mac
p2 = l2/l3/l4/data

