import socket

TIME_OUT = 0.5

class Cliente:
    def __init__(self, host, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_addr = (host,port)
        self.__socket.connect(self.__server_addr)
        self.__socket.settimeout(TIME_OUT)

    def __send(self, operacao, a, b):
        try:
            self.__socket.send(('%s,%s;%s' % (operacao, str(a), str(b))).encode())
            resultado = self.__socket.recv(1024).decode()

            if resultado != '':
                return resultado

        except BrokenPipeError:
            try:
                self = Cliente(self.__server_addr[0], self.__server_addr[1])

            except ConnectionRefusedError:
                return 'O servidor está offline. (CONNECTION REFUSED)'

        except socket.timeout:
            return 'O servidor não respondeu. (TIME OUT)'

        return self.__send(operacao, a , b)

    def soma(self, a, b):
        return self.__send('so', a, b)

    def subtracao(self, a, b):
        return self.__send('su', a, b)

    def divisao(self, a, b):
        return self.__send('di', a, b)

    def multiplicacao(self, a, b):
        return self.__send('mu', a, b)

    def close(self):
        if self.__socket is not None:
            self.__socket.close()
