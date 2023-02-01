from scapy.all import *
from scapy.layers.inet import IP, TCP , UDP,ICMP 
import socket
from geoip import geolite2 


def get_serv(src_p,dst_p):  # To get service by port 
    try:
        service = socket.getservbyport(src_p)
    except:
        service = socket.getservbyport(dst_p)
    return service

#--------------------------------------------------------------

def locate(ip):

    loc = geolite2.lookup(ip)
    if loc is not None:
        return loc.country , loc.timezone ,loc.location
    else:
        return None

#--------------------------------------------------------------

    



def analyzer(pkt):
    try:

        src_ip =  pkt[IP].src  #source ip 
        dst_ip =  pkt[IP].dst  #destnation ip
        loc_src= locate (src_ip)
        loc_dst= locate (dst_ip)
        if loc_src is not None: # To ckeck ip puplic or nono
            country= loc_src[0]
            timezone= loc_src[1]
            location= loc_src[2]
        if loc_dst is not None:
            country= loc_dst[0]
            timezone= loc_dst[1]
            location= loc_dst[2]
        else:
            country= "UnKnown"
            timezone= "UnKnown"
            location= "UnKnown"


        src_mac = pkt.src      #source MAC
        dst_mac = pkt.dst      #destnation MAC
        src_port= pkt.sport    #port is int
        dst_port= pkt.dport
        service = get_serv(src_port , dst_port)

        #-----------------------------------------------------------

        if pkt.haslayer(TCP): # if the packet is TCP
            print("-" *50)
            print("TCP Packet..")

            print("SRC IP -->",src_ip)
            print("DST IP -->",dst_ip)
            print("SRC MAC -->",src_mac)
            print("DST MAC -->",dst_mac)
            print("SRC port -->",str(src_port))
            print("DST port -->",str(dst_port))
            print(f"TimeZone : {timezone} \n country : {country} \n location : {location}")
            print(f"Service is {service}")
            print("Packet Size : " + str(len(pkt[TCP])) + "byte")

            if pkt.haslayer(Raw): #if pkt contian data
                print(pkt[Raw].load) #to dsplay data
            print("-" *50)

        #-----------------------------------------------------------------

        elif pkt.haslayer(UDP):
            print("-" *50)
            print("UDP Packet..")

            print("SRC IP -->",src_ip)
            print("DST IP -->",dst_ip)
            print("SRC MAC -->",src_mac)
            print("DST MAC -->",dst_mac)
            print("SRC port -->",str(src_port))
            print("DST port -->",str(dst_port))
            print(f"TimeZone : {timezone} \n country : {country} \n location : {location}") 
            print("Packet Size : " + str(len(pkt[UDP]))+ "byte")

            if pkt.haslayer(Raw): 
                print(pkt[Raw].load) #to dsplay data
            print("-" *50)

        #-----------------------------------------------------------------

        # elif pkt.haslayer(ICMP):
        #     print("ICMP Packet...........")

    except:
        pass

    
    


    print("-" *50)
    

print("****************STARTED*************************")
sniff(iface="Wi-Fi" , prn= analyzer)

