import re
routefile=open("ShowIpRoute.txt","r")
routelist=routefile.readlines()
capturedlist=["","","","","","",""]
outputfile=open("output.txt","w")

routecodes={None:"","L":"local","C":"connected","S":"static","R":"RIP","M":"mobile","B":"BGP","D":"EIGRP","EX":"EIGRP external","O":"OSPF","IA":"OSPF inter area","N1":"OSPF NSSA external type 1","N2":"OSPF NSSA external type 2","E1":"OSPF external type 1","E2":"OSPF external type 2","i":"IS:IS","su":"IS:IS summary","L1":"IS:IS level:1","L2":"IS:IS level:2","ia":"IS:IS inter area","*":"candidate default","U":"per:user static route","o":"ODR","P":"periodic downloaded static route","H":"NHRP","l":"LISP","a":"application route","+":"replicated route","%":"next hop override","E":"EGP"}
if (routefile.closed == False):
	routefile.close()
for i in range(len(routelist)):
		matchobject=re.search(r"(^.+?) ([A-Z]\d)? ?((\d{1,3}\.?){4}) \[(.+)\].+ ((\d{1,3}\.?){4}), (.+),(.+)",str(routelist[i]))
		if matchobject:
			capturedlist[0]=matchobject.group(1)#firstletter
			capturedlist[1]=matchobject.group(2)#additional code
			capturedlist[2]=matchobject.group(3)#Route
			capturedlist[3]=matchobject.group(5)#Metric
			capturedlist[4]=matchobject.group(6)#Next-hop
			capturedlist[5]=matchobject.group(8)#lastUpdate
			capturedlist[6]=matchobject.group(9)#Outbound Interface
			outputfile.write("\nProtocol:\t"+routecodes[capturedlist[0]]+" "+routecodes[capturedlist[1]]+"\n"+"Prefix:\t\t"+capturedlist[2]+"\n"+"AD/Metric:\t"+capturedlist[3]+"\n"+"Next-hop:\t"+capturedlist[4]+"\n"+"Last Update:\t"+capturedlist[5]+"\n"+"Outbound Int:\t"+capturedlist[6])
			print "\nProtocol:\t"+routecodes[capturedlist[0]]+" "+routecodes[capturedlist[1]]+"\n"+"Prefix:\t\t"+capturedlist[2]+"\n"+"AD/Metric:\t"+capturedlist[3]+"\n"+"Next-hop:\t"+capturedlist[4]+"\n"+"Last Update:\t"+capturedlist[5]+"\n"+"Outbound Int:\t"+capturedlist[6]
		else:
			print routelist[i]
outputfile.close()	
#print routelist