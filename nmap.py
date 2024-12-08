import nmap

def scan_ssh_hosts(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-p 22 --open')

    for host in nm.all_hosts():
        if nm[host]['tcp'][22]['state'] == 'open':
            print(f"Host: {host} (SSH is open)")

network_range = ""  #put the ip range here
scan_ssh_hosts(network_range)
