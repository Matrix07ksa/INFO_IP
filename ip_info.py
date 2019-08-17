# -*- coding: utf-8 -*-
import ipaddress as ip
import re
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray

print ("""
 ______________
||            ||
||            ||
||            ||
||            ||
||____________||
|______________|
 \\############\\
  \\############\\
   \      ____    \   
    \_____\___\____\{Hejab Zaeri}
""")
def main():
	try:
		while True:
			IP_ADDR = str(input(R+'Enter Your IP Address::'))
			IP_ADDR=re.match("\w+\S\w+\S\w+\S+[*.]",IP_ADDR).group()+"0"
			bitmask = str(input(G+"Enter the Bitmask (8-24-30): "))
			net_addr = IP_ADDR + '/' +str(bitmask)
			print(GR+"network address : %s"%net_addr)
			try:
				network = ip.ip_network(net_addr)
				network_version= network.version
				netmask = str(network.netmask)
				print("Version IP: IPV%s"%network_version)
				print("IP_Bit:"+'.'.join([bin(int(x)+256)[3:] for x in IP_ADDR.split('.')]))
			except Exception:
				raise Exception("Failed to create network")
			print(O+"This is prefix will give %s IP addresses"%network.num_addresses+W)
			print(O+"Network configuration will be :")
			print(R+"\t Netmask_Network: %s %s"%(G,str(network.netmask)))
			print(R+"\t Netmask_Bit:"+G+'.'.join([bin(int(x)+256)[3:] for x in netmask.split('.')])+W)
			print(R+"\t Hostmask address: %s%s"%(G,str(network.hostmask))+W)
			print(R+"\t Broadcast address : %s%s"%(G,str(network.broadcast_address))+W)
			print(R+"\t \t Bitmask MAX : %s%s"%(G,str(network.max_prefixlen))+W)
			print(R+"\t \t IP Is Global: %s%s"%(G,str(network.is_global))+W)
			print(R+"\t \t IP Is Private: %s%s"%(G,str(network.is_private)+W))
			first_ip= list(network.hosts())[0]
			last_ip = list(network.hosts())[-1]
			print("\t Host IP addresses: from %s to %s "%(first_ip , last_ip))
			status = str(input("configuration OK exit [Y/N]? "))
			if status == "Y" or status == "y":
                                break
			else:
			     return main()
	except KeyboardInterrupt :
		print("NO Ctrl+c")

if __name__ == '__main__':
	main()	
