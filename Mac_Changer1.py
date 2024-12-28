#! /usr/bin/env python
#Welcome to Mac changer1
print("Welcome to the Mac Changer!")

import subprocess
subprocess.call("ifconfig", shell=True)
interface = input("Enter your Interface:\n")
mac = input("Please enter your New Mac Adress:\n")
subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {mac} ", shell=True)
subprocess.call(f"ifconfig {interface} up ", shell=True)
print("[+] Changing MAC address for " + interface + "to " + mac)
