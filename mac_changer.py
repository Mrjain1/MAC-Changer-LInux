import subprocess
import optparse
import re


def compare(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])  # -- This will show the entire ifconfig wlan0 command's output.
    ifconfig_search = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if ifconfig_search:
        return ifconfig_search.group(0)
    else:
        print("No Mac Address found")


def parser():
    parser2 = optparse.OptionParser()
    parser2.add_option("-i", "--interface", dest='interface', help='Interface')
    parser2.add_option("-m", "--mac", dest='mac', help='Mac Address')
    (options, arguments) = parser2.parse_args()
    if not options.interface:
        parser.error("Please specify interface")
    elif not options.mac:
        parser.error("Please specify mac")
    else:
        return options


def commands(interface, new_mac):
    print("Changing mac address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", 'ether', new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = parser()

current_mac = compare(options.interface)
print("Current MAC = "+current_mac)
commands(options.interface, options.mac)
if current_mac == options.mac:
    print("MAC Has not been changed.")
else:
    print("The Mac has been changed.")