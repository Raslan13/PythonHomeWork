access_template = ['switchport mode access',

'switchport access vlan ',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan ']
interfacemode=""
interface=""
vlannum=[""]
allowedvlans=[]
flag=0
interfacetypeflag=0
while flag!=3:
	vlannum=[""]
	flag=0	
	interfacemode=raw_input("\n\n\n Please Enter interface mode (Access/Trunk): \nChoose : \n1.Access\n2.Trunk \n")
	try:
		if int(interfacemode)!=1 or int(interfacemode)!=2 :
			flag=flag+1
			interfacetypeflag=int(interfacemode)
	except ValueError:
		print" you entered something that is not 1 or 2 !!\n\n"
	if flag==1:
		interface=raw_input("\nPlease Enter interface type and number Example:F0/1 : \n")
		if interface!="":
			flag=flag+1
	
	if interfacetypeflag==1:
		vlannum.append(str(raw_input("\nPlease Enter Vlan number :\n")))
		if vlannum!="":
			flag=flag+1
		if int(vlannum[1])>4095 or int(vlannum[1])<=0:
			flag=flag+1
	if interfacetypeflag==2:
		vlannum.append(str(raw_input("\nPlease Enter list of allowed Vlans, were Vlans are sperated by a comma, ex: 5,6,8 \",\" or range of vlans example 5-100 or both like : 4,8,9,11-113: \n")))
		list2=(vlannum[1].split(","))
		for i in range(len(list2)):
			if "-" in list2[i]:
				
				allowedvlans.append(list2[i])
			else:
				vlannum.append(list2[i])
				try:
					if int(list2[i])>4095 or int(list2[i])<=0:
						flag=flag+1
				except ValueError:
					continue
						
				
		flag=flag+1
	if flag!=3:
		
		print " \nyou didn't follow the rules to input the data please reenter your information!!! \n "
	#flag is raised when something wrong is entered or doesn't match the pattern, the program will keep raising the flag until a correct input is matched and then we can exit the loop
print"\n\n\nResult:\n\n\n " 
if int(interfacemode)==1:
	for i in range (len (access_template)):
		if i!=1:
			print str(access_template[i])
		else:
			print str(access_template[i])+""+str(vlannum[1])
			
list3=vlannum[2:]
for i in range (len(list3)):
	list3[i]=list3[i]+","
for i in range (len(allowedvlans)):
	allowedvlans[i]=allowedvlans[i]+","	
	
if int(interfacemode)==2:
	for i in range (len (trunk_template)):
		if i!=1:
			print str(trunk_template[i])
		else:
			print str(trunk_template[i])+" "+str("".join(list3))+str("".join(allowedvlans))


	