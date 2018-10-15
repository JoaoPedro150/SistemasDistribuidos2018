import socket
import threading

class Servidor:
    def __init__(self, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(('',port))
        self.__socket.listen(5)

    def start(self):
        while True:
            connection = self.__socket.accept()
            threading.Thread(target=self.__newConnection, args=([connection[0]])).start()
        return 0

    def __newConnection(self, client):
        msg = client.recv(1024).decode()

        while msg != '':
            threading.Thread(target=self.__newRequest, args=([client, msg])).start()
            msg = client.recv(1024).decode()

    def __newRequest(self, client, msg):
        operacao = msg.split(',')

        msg = operacao[1]
        msg = msg.split(';')

        operacao = operacao[0]

        resultado = 0

        if operacao == 'so': resultado = float(msg[0]) + float(msg[1])
        elif operacao == 'su': resultado = float(msg[0]) - float(msg[1])
        elif operacao == 'mu': resultado = float(msg[0]) * float(msg[1])
        elif operacao == 'di':
            if msg[1] == '0.0':
                resultado = 'Impossível dividir por 0.'
            else:
                resultado = float(msg[0]) / float(msg[1])

        client.send(str(resultado).encode())

    def close(self):
        if (self.__socket):
            self.__socket.close()

if __name__ == '__main__':
    import os
    os._exit(Servidor(12346).start())
