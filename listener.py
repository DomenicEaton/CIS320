import socket
print('starting dupserver.py')
SERVER_HOST_STR = ''
SERVER_PORT_INT = 12000
SERVER_ADDRESS_TUPLE = (SERVER_HOST_STR, SERVER_PORT_INT)
MAX_BYTES_RX_INT = 2048
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as active_socket:
        active_socket.bind(SERVER_ADDRESS_TUPLE)
        print('The echo server is ready to recieve and SEND BACK')
