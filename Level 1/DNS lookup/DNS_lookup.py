import dns.resolver as dns_r

target = str(input("Enter Domain Name / IP For Target >>: "))

type =["A" , "AAAA" , "MX" , "NS" , "SOA" , "SRV" , "CNAME" ]

for record in type:

    d = dns_r.query(target ,record , raise_on_no_answer=False )
    
    if d.rrset is not None:

        print(f"Record {record} is  {d.rrset}")
