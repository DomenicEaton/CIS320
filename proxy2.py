#!/usr/bin/python3
import socket

print('I am the webserver')
with socket.socket() as s:
  print('I created a socket')
  s.bind(('',12001))
  print('I binded')
  print('starting to listen')
  s.listen(1)
  print('I am listening, waiting for an accept')
  conn, addr = s.accept()
  print('I accepted a connection from:' , addr)
  request = conn.recv(2048)

  #get the target html file name
  request_list = request.decode().split()
  print('request list:', request_list)
  target = request_list[1]
  target = target[1:]
  print('the target is', target)


  #get target website



  c = socket.socket()
  # replace niagaracomputing.org with the external IP address of your server
  c.connect((target, 80)) # recall 80 is the required http port #

  # replace niagaracomputing.org with the external IP address of your server
  c.sendall('GET / HTTP/1.1\r\n'.encode())
  cd = 'Host:' + target + '\r\n'
  c.sendall(cd.encode())
  c.sendall('\r\n'.encode())
  response = c.recv(2048)
  print(response.decode())
  print('target acquired')
  c.close()






  #after we get response, send back to original conn
  conn.send(response)
  print('sent response')
  print('closing conn')
  conn.close()
