# port scanner
import  socket

ipaddr = "127.0.1.1"
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
timeout = socket.getdefaulttimeout()

def ScanFor(ip,port):
	try:
		if timeout is None:
			socket.setdefaulttimeout(0.5)
		socks.connect((ip,port))
		return ('Open')
	except:
		return None



for portno in range(100):
	v = ScanFor(ipaddr,portno)
	if v is not None:
		print("port {0} is -> {1}".format(portno,v))


socks.close()