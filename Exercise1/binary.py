octet=["","","",""]
def Binary_address(ip=[" "]):
	for i in range(len(ip)):
		ip[i]=int(ip[i])
		#result will be in the form of 0b0010
		octet[i]=(bin(ip[i])).replace("b","0")
		#this is to replace the "b" with zero

	for i in range(len(octet)):
		octet[i]=(10-len(octet[i]))*"0"+octet[i]
	#this is to add additional zeros from the front to make it 10 charachters#
	
	return octet