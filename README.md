This is the Python Module HomeWork
All codes and functions are created by me from the Scratch to test my learning ability after watching GNS3 Academy Videos!
Codes are written using Python Version: 2.7.14

Exercise 1 Features & Output:
-To Run the application, just run main.py
-Checks the validity of the IP Address in the form of xxx.xxx.xxx.xxx, where xxx is not greater than 255.
-Checks the validity of NetMask Address it should be in the form of xxx.xxx.xxx.xxx also ex. 255.255.192.128 is not accepted, but ex.255.255.0.0 is accepted.
-Converts to the IP Address into binary.
-Outputs the Broadcast address.

Output example:

IP address is : [192, 168, 1, 25]
NetMask address is : [255, 255, 0, 0]
Binary IP address is : ['0011000000', '0010101000', '0000000001', '0000011001']
Network address is : [192, 168, 0, 0]
Broadcast address is : [192, 168, 255, 255]

Exercise 2 Features & Output:
-To Run the application, just run Exercise2.py
-Reads trunk allowed VLANs via a regex from a text file
-Creates a baseline of all captured valid available VLANs.
-Counts the number of occurring vlans and compare it to the number of the lines captured, so if the same vlan exists on all lines, means its common, and if it just appeared once, means its a unique one.
- Order the output in ascending order.

Output example:

list of Common Vlans [5, 8, 111]

list of Unique Vlans[3, 10, 15, 21, 23, 25, 44, 75, 88, 100, 112, 113]

Exercise 3 Features & Output:
-To Run the application, just run Exercise3.py
-Reads show ip route command output in the text format file.
-Created Dynamic Dictionary for Route Codes.
-Regex to Capture Dynamic routes, with there exact codes ex ( O-OSPF, E-EGP) also able to identify routes with more accurate type like (O E2)
-The output is displayed in more Friendly and understandable format in a text file and printed on the screen.

Output example:

Protocol:       IS:IS level:2
Prefix:         10.89.66.0
AD/Metric:      115/20
Next-hop:       10.89.64.240
Last Update:    0:00:12
Outbound Int:    Ethernet0



Protocol:       NHRP
Prefix:         172.16.99.0
AD/Metric:      250/1
Next-hop:       10.1.1.99
Last Update:    00:11:43
Outbound Int:    Tunnel0

Exercise 4 Features & Output:
-To Run the application, just run Exercise4.py
-Outputs the desired Switch command.
-Choose between 1 for access or 2 Trunk,instead of typing the whole word, does a validity check.
-The user enters his desired interface type.
-After that, it promotes him to enter the vlans in range ex. 5-16 , or separated by commas.

Output example:

switchport trunk encapsulation dot1q
switchport mode trunk 4,9,8,11-120
switchport trunk allowed vlan

 
