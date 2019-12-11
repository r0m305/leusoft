# leusoft
Written by Romeos CyberGypsy
[+] Deauthenticate users from an AP...
[-] Your network interface should be in monitor mode
[-] Run the following command in your terminal: airmon-ng  start <interface_name>

Usage: romeos_AP_deauth.py [options]

Options:
  -h, --help            show this help message and exit
  -g GATEWAY, --gateway=GATEWAY
                        MAC Address of gateway
  -i INTERFACE, --interface=INTERFACE
                        Intended interface to use e.g wlan0
  -p PACKETS, --packets=PACKETS
                        Deauthentication packets to throw
