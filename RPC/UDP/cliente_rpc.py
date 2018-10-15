import socket
import protocolo

MAX_TENTATIVAS = 4
TIME_OUT = 0.5

class Cliente:
    def __init__(self, host, port):
        self.__addr = (host, port)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.settimeout(TIME_OUT)

    def __send(self, operacao, a, b):
        num_tentativas = 1

        while (True):
            try:
                self.__socket.sendto(protocolo.to_client_format(operacao, a, b).encode(), self.__addr)
                return protocolo.get_client_data(self.__socket.recvfrom(1024)[0].decode())

            except socket.timeout:
                if (num_tentativas == MAX_TENTATIVAS):
                    return 'O servidor não respondeu a solicitação.'
                else:
                    num_tentativas += 1

    def soma(self, a, b):
        return self.__send('1', a, b)

    def subtracao(self, a, b):
        return self.__send('2', a, b)

    def multiplicacao(self, a, b):
        return self.__send('3', a, b)

    def divisao(self, a, b):
        return self.__send('4', a, b)

    def close(self):
        if self.__socket is not None:
            self.__socket.close()
