import socket

HOST = "127.0.0.1"
PORT = 8000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Para sair use CRTL+X'
msg = raw_input('Voce: ')
while msg <> '\x18':
	udp.sendto (msg, dest)
	msg = raw_input('Voce: ')
udp.close
