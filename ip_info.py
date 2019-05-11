import ipaddress as ip
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
			IP_ADDR = str(input(R+"Enter Your IP Address::"))
			bitmask = input(B+"Enter the Bitmask (24-30): ")
			bitmask = int(bitmask)
			net_addr = IP_ADDR + '/' +str(bitmask)
			print(GR+"network address : %s"%net_addr)
			try:
				network = ip.ip_network(net_addr)
				network_version= network.version
				print("Version IP: IPV%s"%network_version)
			except:
				raise Exception("Failed to create network")
			print("This is prefix will give %s IP addresses"%network.num_addresses)
			print("Network configuration will be :")
			print("\t network address: %s"%str(network.netmask))
			print("\t Witcard address: %s"%str(network.hostmask))
			print("\t Broadcast address : %s"%str(network.broadcast_address))
			print("\t \t Bitmask MAX : %s"%str(network.max_prefixlen))
			print("\t \t IP Is Global: %sKeyboardInterrupt"%str(network.is_global))
			print("\t \t IP Is Private: %s"%str(network.is_private))
			  
				
			first_ip= list(network.hosts())[0]
			last_ip = list(network.hosts())[-1]
			print("\t host IP addresses: from %s to %s "%(first_ip , last_ip))
			status = str(input("configuration OK exit [Y/N]? "))
			if status =='Y' or 'y':
				exit()
	except KeyboardInterrupt :
		print("NO Ctrl+c")

if __name__ == '__main__':
	main()	
