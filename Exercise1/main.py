import IP
import Subnet
import binary
import NetworkBroadAddress
ipaddress=IP.ip_address()
netmask=Subnet.Subnet()
binary=binary.Binary_address(ipaddress)
NetworkAddress=NetworkBroadAddress.NetworkAddress(ipaddress,netmask)



print"\n"+"IP address is : "+str(ipaddress)+"\n"+"NetMask address is : "+str(netmask)+"\n"+"Binary IP address is : "+str(binary)+"\nNetwork address is : "+str(NetworkAddress)+"\nBroadcast address is : "+str(NetworkBroadAddress.Broadcast)
