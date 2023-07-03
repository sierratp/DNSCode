import subprocess
import csv
import socket
import nmap


# checks ping if host is reachable or not
def testPing1():

    o = open('output2.csv', 'w', newline='')
    outfile = csv.writer(o)
    with open('dns-mfh-local-export.csv', 'r') as file:
        infile = csv.reader(file, delimiter=',')
        next(infile)
        for row in infile:
            hostname = row[2]
            try:
                ip_addresses = socket.gethostbyname_ex(hostname)[-1]
                for ip_address in ip_addresses:
                    command = ["ping", "-n", "1", ip_address]
                    is_successful = subprocess.call(command) == 0

                    if is_successful:
                        #print(hostname + " (" + ip_address + ") is open.")
                        outfile.writerow([hostname , "accessible"])
                    else:
                        #print(hostname + " (" + ip_address + ") is closed.")
                        outfile.writerow([hostname , "not accessible"])
            except socket.gaierror:
                outfile.writerow(["Failed to resolve IP address for " , hostname])




testPing1()