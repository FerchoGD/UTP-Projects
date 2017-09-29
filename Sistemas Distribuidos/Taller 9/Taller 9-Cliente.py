import time
import xmlrpc.client

s=xmlrpc.client.ServerProxy('http://localhost:5000')


while True:
	hora=s.Tiempo()
	print(time.ctime(hora))
	time.sleep(2)