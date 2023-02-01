from scapy.all import ARP , Ether , srp 
import sys

exist = []

def scan(ip):

    print("IP \t\t\t\t\t\t MAC")
    print("-" * 100)

    while True:

        try:
            arp_req= ARP(pdst=ip) # dstnetion ip 

            brodcast = Ether(dst="ff:ff:ff:ff:ff:ff") #dstnation mac

            arp_brodcast = brodcast / arp_req # make brodcast in ip 

            res = srp(arp_brodcast , timeout = 3 , verbose =False)[0] #send and receive packets at layer 2 

            # print (res)                                          # 0 --> the dvies is replay  , 1 -- > the dvies are not replay

            lst = []

            for element  in res:

                client = {"ip" : element[1].psrc , "mac" : element[1].hwsrc} #psrc == ip src  , hwsrc == src mac
                lst.append(client)



            for i in lst:

                if i['mac'] not in exist:
                         print(f"  {i['ip']} \t\t\t\t\ {i['mac']} ")
                         exist.append(i['mac'])

        except:
            print("\Exit..!")
            sys.exit()


ip = "192.168.1.1/24"

result_list = scan(ip)





