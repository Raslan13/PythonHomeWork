def ip_address():

	iplist=[" "]
	flag=0
	while len(iplist)!=4 or flag!=0:
		#it will keep asking to enter correct ip address until its in correct format
		#and in valid one between 0.0.0.0-255.255.255.255
		ip=raw_input("\nPlease enter a Valid Ip address in the form of xxx.xxx.xxx.xxx were xxx is from 0 to 255: \n")
		iplist=ip.split(".")
		flag=0
		#print flag
		#print iplist
		if len(iplist)==4:
			for index in range (len(iplist)):
				testnumber=int(iplist[index])
				if testnumber >255 or testnumber<0:
					flag=flag+1
		else:
			flag=flag+1
		if flag!=0:
			print" \n!!!!!Invalid IP Please renter your IP!!!!!\n"
		#print str(flag)+"after enteringloop"
	
	return iplist
	