import socket
import threading
import hashlib
import protocolo

class Servidor:
    def __init__(self, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(('',port))

    def start(self):
        while(True):
            data, client_address = self.__socket.recvfrom(1024)
            self.__novaRequisicao(data, client_address)

    def __novaRequisicao(self, data, client_address):

        msg = protocolo.get_server_data(data.decode())

        if (msg == None):
            return

        resultado = 0

        if (msg[0] == '1'):
            resultado = msg[1] + msg[2]
        elif (msg[0] == '2'):
            resultado = msg[1] - msg[2]
        elif (msg[0] == '3'):
            resultado = msg[1] * msg[2]
        elif (msg[0] == '4'):
            if (msg[2] == 0):
                resultado = 'Impossivel dividir por 0.'
            else:
                resultado = msg[1] / msg[2]

        self.__socket.sendto(protocolo.to_server_format(resultado).encode(), client_address)

    def close(self):
        if (self.__socket):
            self.__socket.close()

if __name__ == '__main__':
    import os
    os._exit(Servidor(12346).start())
