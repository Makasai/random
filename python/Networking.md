##Argument Parsing
####argparse

parser = argparse.ArgumentParser(description="")  
parser.add_argument('-i', type=str, help="", required=True)  

* '-i' is the variable (or flag?) that is passed after calling the script
	* i.e. python test.py -i some_str 
* type: signifies what type of data that variable/flag accepts
* cmdargs = parser.parse_args(): puts all added argumnts together
* cmdargs.i : variables/flags are saved as attributes of cmdargs


##Byte Order
When computer writes out data, it needs to remember the order

big endian - writing bytes with most significant (largest?) byte is first and then descending order  
i.e: 1 2 3 4

* first byte  - 1000  
* second byte - 200   
* third byte  - 30  
* fourth byte - 4  

little endian - opposite of big endian

Intel systems writes using little endian. But other systems use big endian. This is important because how do you send data between systems if they don't follow the same endian? Therefore, the standard for sending data needs to be put in 'Network byte order'.

Network byte order - big endian

There are functions to change endian to Network byte order

##Lookups
IP address or by name

import socket (old unix library)
socket.gethostbyaddr  -  reverse DNS lookup
socket.gethosebyname
SOCK_STREAM = TCP
family = Internet

Chapter 3/NetworkClient.py

- make sure there is a server running on that port
	- nc -l <port>
- send a stream of bytes, not a python string
	- b"this is a message"


##Banner
Banner headers contain information about the server, such as the company that owns the server


##SMTP
mail service

send message via SMTP, need to retrieve it

	import smtplib
	s = smtplib.SMTP(<ip of server>, <port>) #This is the SMTP object
	s.sendmail(<src address>, <dest address>, <message>")
	 
	 
	  