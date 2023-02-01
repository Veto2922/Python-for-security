import socket as sk

target= input(str("Inter the ratget :  "))
# p= 19
# "172.217.171.206"  --> google ip
# ports =[19, 20 , 21 , 22 , 23  , 25 , 80 , 443]
ports = range(19, 101)

for p in ports:
        s= sk.socket(sk.AF_INET , sk.SOCK_STREAM) #use ipv4 and TCP connection
        
        s.settimeout(1) #if don't reseve replay weit  1 sec then drop connection

        r= s.connect_ex((target , p)) #retean states code EX (0 mean the port is open) (11 or 111 mean port is close)

        if r == 0:
            
            try:
                service = sk.getservbyport(p) #to get name of service by number of port
                

                print(f"--[ *Port {p} * is open  --> {service} ]")
                

            except:  
                continue


        else:
            print(f"-- Port {p} is close")

        s.close()



