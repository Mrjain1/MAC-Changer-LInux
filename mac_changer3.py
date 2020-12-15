#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

"""Here in this piece of code we can see that we can put the interface and mac address that 
we need to change for a specific Interface and we can also do a listing of the files of a specific directory."""

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="Interface", help="This will specify the interface whose MAC Address needs to be changed.")
parser.add_option("-m", "--mac", dest="new_mac", help="Here specify the desired MAC address to change")
(options, argument) = parser.parse_args()

change_mac(options.Interface, options.new_mac)
