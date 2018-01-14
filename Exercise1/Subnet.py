def Subnet():
	netlist=[" "]
	flag=0
	flag2=0
	knownnetmasks=[0,128,192,224,240,248,252,254,255]
	while len(netlist)!=4 or flag!=4 or flag2!=0:
		#it will keep asking to enter correct Netmask until its entered
		#it wont exit the loop until the formating of the subnet is correct and the numbers are correct 
		net=raw_input("\nPlease enter netmask address in the form of xxx.xxx.xxx.xxx: \n")
		netlist=net.split(".")
		flag=0
		flag2=0
		#print flag
		#print flag2
		#print netlist
		#print"\n"
		if len(netlist)==4:
			for index in range (len(netlist)):
				testnumber=int(netlist[index])
				for index2 in range(len(knownnetmasks)):
					testnumber3=int(knownnetmasks[index2])
					if testnumber == testnumber3:
						flag=flag+1
						#flag is raised only on matching number of subnet
				if index<3:
					testnumber2=int(netlist[index+1]) 
					if testnumber2>testnumber :
						flag2=flag2+1		
						#flag is raised if current number is larger than the previous number
						#in subnet that is impossible
					if (testnumber2!=255 and testnumber2!=0) and (testnumber!=255 and testnumber !=0):
						testnumber2==testnumber
						flag2=flag2+1
						print"we have a match"
						#flag to raise if the current number is equal to the next one like 255.192.192.0 no acceptable)
		if flag!=4 or flag2!=0:
			print"  !!!!!Invalid Subnet Please renter your Subnet!!!!!\n"
		#print str(flag)+ " "+str(flag2)+" after enteringloop"
	return netlist