import subprocess
import optparse

def parser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest='interface', help='Interface')
    parser.add_option("-m", "--mac", dest='mac', help='Mac Address')
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("Please specify interface")
    elif not options.mac:
        parser.error("Please specify mac")
    else:
        return options


def commands(interface, new_mac):
    print("Changing mac address of "+interface+" to "+new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", 'ether', new_mac])
    subprocess.call(["ifconfig", interface, "up"])



options = parser()
commands(options.interface, options.mac)