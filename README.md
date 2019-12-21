[+] Written by Romeos CyberGypsy
[+] Deauthenticate specified or all users from a wifi network
 
[!] This script is only for educational purposes. 
Do not use it to cause harm 
I will not be responsible for misuse of this script!!
 
For any query, get in touch at lewiswaigwa30@gmail.com
(C) Leusoft Revived
 
[!] Before using this script, Ensure that your network interface is in monitor mode by running the following commands in your terminal:
airmon-ng start <interface> or ifconfig <interface> mode monitor
Usage: romeos_AP_deauth.py [options]

Options:
  -h, --help            show this help message and exit
  -s CIDR, --scan-network=CIDR
                        Scan an entire CIDR subnet
  -t TARGET, --target=TARGET
                        Deauthenticate a specific target via MAC Address.
                        Defaults to ff:ff:ff:ff:ff:ff, for broadcasting
  -g GATEWAY, --gateway=GATEWAY
                        MAC Address of the network's gateway
  -i INTERFACE, --interface=INTERFACE
                        Intended network interface to work with e.g wlan0
  -p PACKETS, --packets=PACKETS
                        Deauthentication packets to throw
  -l LOOP, --loop=LOOP  Number of times to send the deauthentication packets.
                        Defaults to 1

EXAMPLE USAGES
To scan a network for discovery of active hosts alongside their MAC Addresses, type:
	python romeos_AP_deauth.py -s <CIDR>
	CIDR represents the ip addresses of a local subnet e.g 192.168.43.1/24

To deauthenticate all users from an AP, type:
	python romeos_AP_deauth.py -g <gateway mac address> -i <wireless_interface_name> -p <number_of_deauth_packets_to_send> -l <loop>
	e.g python romeos_AP_deauth.py -g fe:6f:44:61:f1:57 -i wlan0 -p 100 -l 5

To deauthenticate a specific user from an AP, type:
	python romeos_AP_deauth.py -t <target_mac_address> -g <gateway_mac_address> -i <wireless_interface_name> -p <number_of_deauth_packets_to_send> -l <loop>

To view help, type:
	python romeos_AP_deauth.py -h or --help