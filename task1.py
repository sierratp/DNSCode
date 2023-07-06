import subprocess
import csv
import socket as sock
import nmap



# uses subprocess
# notes: I think works, takes about 2-3 seconds for each input so could take a long time to do entire file 
def testPort1():
    with open('test3.csv', 'r') as file:
        infile = csv.reader(file,delimiter=',')
        next(infile)
        for row in infile:
            command = ["ping", "-n", "1", row[2]]
            isSuccessful =subprocess.call(command) == 0
            

            if isSuccessful:
                print(row[0] + ' is open.')
            else:
                print(row[0] + ' is closed.')


#uses nmap
def testPort2():
    nm = nmap.PortScanner()


# uses socket
# notes: gives closed for all, including my own IP; could be due to the destination and reading the file 
def testPort3():
    print("socket trial ")
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    s.settimeout(3)

    #writes output to csv file
    o = open('output.csv', 'w', newline='')
    outfile = csv.writer(o)

    with open('test3.csv', 'r') as file:

        infile = csv.reader(file,delimiter=',')
        #next(infile)

    
        for row in infile:
            # add exception if empty row 
            destination = (row[2], 5985)

            try:
                t = s.connect_ex((destination))

                if t == 0:
                    #outfile.writerow([row[0] + " is open"])
                    outfile.writerow([row[0] , "open"])
                else:
                    # outfile.writerow([row[0] + " is not open"])
                    outfile.writerow([row[0] , "closed"])
                
            except:
               outfile.writerow(["error reading data"])
               '''
                try: 
                    destination = (row[0], 5985)
                    t = s.connect_ex(destination)

                    if t == 0:
                        #outfile.writerow([row[0] + " is open"])
                        outfile.writerow([row[0] , "open"])
                    else:
                        # outfile.writerow([row[0] + " is not open"])
                        outfile.writerow([row[0] , "closed"])

                
                
                except:
               '''
               
        s.close()
        o.close()

    print("results in output file")

# uses sockets 
# WORKING??? gives open ports, still can't read last files 
def testPort4(host, port):
    with open('output.csv', 'a', newline='') as o:
        outfile = csv.writer(o)
        try:
            s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
        
            if result == 0:
                outfile.writerow([host,"open"])
            else:
                outfile.writerow([host,"closed"])
        
            s.close()

        except:
            outfile.writerow([host,"error"])


def openPortTester():
    with open('test3.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) >= 2:
                host = row[2]
                testPort4(host, 5985)
            else:
                print("cannot read csv file")
    print("finished reading")


openPortTester()






    

    
    



'''
#tests connectivity 
Test-WSMan -ComputerName Test1-Win2k12


'''



