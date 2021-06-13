def chat_app():
	import socket
	import threading
	import time
	y_port = 1234
	y_ip = ""
	s_ip = "192.168.29.200"
	s_port = 2345
	name = input("Enter Friend Name : ")
	print("--------------------------  Start Chatting With "+ name + "  --------------------------")
	def recv_d(yy_ip,yy_port):
		sr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sr.bind((yy_ip,yy_port))
		sr.listen()
		while True:
			se,add = sr.accept()
			r_data = se.recv(1024)
			print("Message Received : " + r_data.decode())
			if r_data == 'byby':
				break
			time.sleep(0.1)



	def send_d(ss_ip,ss_port):
		while True:
			ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s_data = input()
			ss.connect((ss_ip,ss_port))
			ss.send(s_data.encode())
			print("Message Send : " + s_data)
			if s_data == 'byby':
				break
			time.sleep(0.1)
			

	send_t = threading.Thread(target = send_d , args = (s_ip,s_port))
	recv_t = threading.Thread(target = recv_d , args = (y_ip,y_port))
	recv_t.start()
	send_t.start()



chat_app()
