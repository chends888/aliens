# Camada Fisica da Computacao
# Exemplo socket server 
## https://pymotw.com/3/socket/tcp.html

import socket
import sys

class Server():

	def __init__(self):
		self.PORTA = 1234
    	# Create a TCP/IP socket

	def connectSocket(self):
	    
	    print("Initializing socket TCP/IP")
	    # Bind the socket to the port
	    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    self.server_address = ('localhost', self.PORTA)
	    print("PORTA {}".format(self.PORTA))
	    self.sock.bind(self.server_address)

	    # Listen for incoming connections
	    sock.listen(1)

	    while True:
	        # Wait for a connection
	        print("Waiting for a connection")
	        connection, client_address = sock.accept()

	        try:
	            print(" connection from {}".format(client_address))
	        except:
	        	pass
	        break
	
	def receberTexto():
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print("{}".format(data))
            if len(data) > 0:
            	return data
            if(len(data) <= 0):
                break

    def finishConnection():
    	finally:
        	# Clean up the connection
        	connection.close()