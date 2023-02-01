from geoip import geolite2

ip="157.205.207.130"

locator = geolite2.lookup(ip)  #get info about this ip

if locator is None:
    print("unKnown")

else:
    print(locator)