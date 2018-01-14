import re
vlanslist=[]
set1=set(vlanslist)
tempstr=""
list3=[]
list4=[]
list5=[]
commandsfile=open("commands.txt","r")
commandslist=commandsfile.readlines()
if (commandsfile.closed == False):
	commandsfile.close()
#print commandslist
for i in range(len(commandslist)):
	tempstr=re.findall(r"al.+v.+[0-9]{1,3},?",commandslist[i])
	if(tempstr!=[]):
		vlanslist.append(tempstr)
	#to capture "allowed vlan x,x,x,x,x" part to ensure correct command is captured 
	#as there exists many other commands with vlan lists but we want that exact one
	
#print vlanslist	
for index1 in range(len(vlanslist)):
	vlanslist[index1]=str(vlanslist[index1])[15:-2]
	#removing the "allowed vlan" keyword
	list1=vlanslist[index1].split(",")
	for index2 in range(len(list1)):
		set1.add(list1[index2])
	#addding all vlans in a set" to remove repeated charachters and to create a baseline for comparing
	
list2=list(set1)
#print list2
for i in range (len(list2)):
		list3.append(0)
		list2[i]=int(list2[i])
		#creating a same size list but with zeros to count occuring numbers for comparing
list2.sort()		
#print list2
#print list3
for index1 in range(len(vlanslist)):
	list1=vlanslist[index1].split(",")
	#print list1
	for index2 in range (len(list1)):
		for index3 in range(len(list2)):
			#print int(list1[index2])
			#print int(list2[index3])
			if int(list1[index2])==int(list2[index3]):
				list3[index3]=list3[index3]+1
				#will take each element from a temp list and compare it against all vlans list to see how many times each vlan occured
	
for i in range (len(list3)):
	if list3[i]==len(vlanslist):
		list4.append(list2[i])
		#if vlans number is equal to the number of lines i passed to my code, it means it appeared on all lines, means its common between all
	if	list3[i]==1:
		list5.append(list2[i])
		#if vlan only appear one it means its unique
#print list3
print "\nlist of Common Vlans "+str(list4)
print"\nlist of Unique Vlans"+str(list5)

#print vlanslist	
#print set1
#print list3


