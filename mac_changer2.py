#!/usr/bin/env python

import subprocess
interface = input("Enter the interface >")
new_mac = input("Enter the Mac Address >")

print("Changing MAC address for "+interface+" to "+new_mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
subprocess.call(["ifconfig", interface, "up"])