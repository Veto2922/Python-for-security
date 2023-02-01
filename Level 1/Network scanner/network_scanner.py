from scapy.all import ARP , Ether , srp 


def scan(ip):

    arp_req= ARP(pdst=ip) # dstnetion ip 

    brodcast = Ether(dst="ff:ff:ff:ff:ff:ff") #dstnation mac

    arp_brodcast = brodcast / arp_req # make brodcast in ip 

    res = srp(arp_brodcast , timeout = 3 , verbose =True)[0] #send and receive packets at layer 2 

    print (res)                                          # 0 --> the dvies is replay  , 1 -- > the dvies are not replay

    lst = []

    for element  in res:

        client = {"ip" : element[1].psrc , "mac" : element[1].hwsrc} #psrc == ip src  , hwsrc == src mac , to decod resalt
        lst.append(client)

    print("IP \t\t\t\t\t\t MAC")
    print("-" * 100)

    for i in lst:
        print(f"  {i['ip']} \t\t\t\t\ {i['mac']} ")


ip = "192.168.1.1/24"

result_list = scan(ip)





