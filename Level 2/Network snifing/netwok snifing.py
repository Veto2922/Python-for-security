import scapy.all as scapy

from scapy.layers import http



def sniffer(interface):

    print("-" *100)
    print("[+]  * Sniffer Has Started ...!  * [+]")
    print("-" *100)

    scapy.sniff(iface=interface, store = False  , prn = procces)
    

def procces(packet):
    
    if packet.haslayer(http.HTTPRequest): # is this packet is http or not

        print("[+] " , packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path) # print the host name if work by http

        print("-------> Response is : " , packet[http.HTTP])
        print("-------> Respo ---------------------------->>>> : " , packet[http.HTTPRequest])

        if packet.haslayer(scapy.Raw):

            req = packet[scapy.Raw].load

            print("[*_*] ->--->--->" ,req)

    # else :

    #     print ("other" , packet)    

sniffer("Wi-Fi")



