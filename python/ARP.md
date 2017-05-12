#Routing/Network

##Routing Table
[http://www.thegeekstuff.com/2012/04/route-examples/](http://www.thegeekstuff.com/2012/04/route-examples/)

Destination of packet is an IP address

* If the destination is in range (192.168.1.0 = 192.168.1.0 - 192.168.1.255), then ARP is used to send packet
* If the destination is not in range, then packet gets sent to a "gateway"

you can set the default gateway:

<br/>
<br/>

##ARP - Address Resolution Protocol
* ARP cache - host device will keep a mapping of MAC and ip addresses of all other network devices that the host has already communicated with

ARP Cache Poisoning: [http://www.thegeekstuff.com/2012/01/arp-cache-poisoning/](http://www.thegeekstuff.com/2012/01/arp-cache-poisoning/)

####How ARP Works
1. (ARP Requst) Machine asks on network, "Who has this IP?"
2. (ARP Resonse) Only the machine with matching IP responds, and sends it's MAC address to requesting machine   
 ??  
 __What if requesting machines receives multiple MAC address__  
 ??  
Unfortunately, there are no authentication checks with this protocol, so anyone could send a legit ARP Response, and have the IP map to another MAC

##Virtual IP Address (VIP)

[scale-out-blog.blogspot.com/2011/01/virtual-ip-addresses-and-their.html](scale-out-blog.blogspot.com/2011/01/virtual-ip-addresses-and-their.html)

* essentially movable IP addresses on a network
