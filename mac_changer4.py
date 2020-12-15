import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='This is to specify the Interface')
    parser.add_option('-m', '--mac', dest='mac', help='This is to specify the Mac Address')
    return parser.parse_args()




def commands(interface, new_mac):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

(options, arguments)= get_arguments()
commands(options.interface, options.mac)
print("[+] Changing the MAC Address for "+options.interface+" to "+options.mac)