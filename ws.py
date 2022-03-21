#!/usr/bin/python3
import socket

print('I am the webserver')
with socket.socket() as s:
  print('I created a socket')
  s.bind(('',12000))
  print('I binded')
  print('starting to listen')
  s.listen(1)
  print('I am listening, waiting for an accept')
  conn, addr = s.accept() # blocks
  print('I accepted a connection from:' , addr)
  request = conn.recv(2048)

  #get the target html file name
  request_list = request.decode().split()
  target = request_list[1]
  target = target[1:]

  print('the request is:', request.decode())

  print('the target is', target)



  resp = 'HTTP/1.0 200 OK\n\n'
  resp += '\n\n'
  #resp += '<h1>Hello World</h1>\n\n'
  f = open('file1.html','r')
  file_str = f.read()
  resp += file_str


  resp = resp.decode()
  conn.sendall(resp.encode())
  print('sent response')
  print('closing conn')
  conn.close()
