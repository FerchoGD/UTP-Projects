import time
import xmlrpc.client

s=xmlrpc.client.ServerProxy('http://localhost:5000')


while True:
	horalocal=time.time()
	print(time.ctime(horalocal))
	horareal=s.Tiempo(horalocal)
	print(time.ctime(horareal))
	time.sleep(2)