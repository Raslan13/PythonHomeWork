Network=[0,0,0,0]
Broadcast=[0,0,0,1]
SubnetDict={128:128,192:64,224:32,240:16,248:8,252:4,254:2,255:1}
def NetworkAddress(ip,subnet):
	for i in range(len(ip)):
	#Convert to int for manipulation and checking
		ip[i]=int(ip[i])
		subnet[i]=int(subnet[i])
		
	for i in range(len(ip)):
		
		if subnet[i]<=255 and subnet[i]>0 :
			Network[i]=((ip[i]/(SubnetDict[subnet[i]]))*SubnetDict[subnet[i]])
			Broadcast[i]=((ip[i]/(SubnetDict[subnet[i]]))*SubnetDict[subnet[i]])+(SubnetDict[subnet[i]]-1)
		if subnet[i]==0:
			Broadcast[i]=255
			Network[i]=0

	
	return Network
	