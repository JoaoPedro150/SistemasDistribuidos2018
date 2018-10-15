import socket
import json
import util
import constantes

class Cliente:
    def __init__(self, host, port):
        self.__name_server_addr = (host, port)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.settimeout(constantes.TIME_OUT)

    def __send_to_operation_server(self, operacao, a, b, list_server):
        num_tentativas = 0
        max_tentativas = constantes.MAX_ATTEMPTS * len(list_server)
        i = 0;

        while True:
            try:
                self.__socket.sendto(util.set_server_operacao_format(operacao, a, b).encode(), list_server[i])
                return util.get_format(self.__socket.recvfrom(constantes.BUFFER_SIZE)[0].decode())
            except socket.timeout:
                if (num_tentativas == max_tentativas):
                    return constantes.NO_SERVER_OPERATION_REPLY_MSG_ERROR
                else:
                    i += 1
                    num_tentativas += 1

                    if (i == len(list_server)):
                        i = 0;

    def __request_operation_server_addr(self, operacao):
        num_tentativas = 1

        while True:
            try:
                self.__socket.sendto(util.set_format(operacao).encode(), self.__name_server_addr)
                return util.get_format(self.__socket.recvfrom(constantes.BUFFER_SIZE)[0].decode())

            except socket.timeout:
                if (num_tentativas == constantes.MAX_ATTEMPTS):
                    return constantes.NO_SERVER_NAME_REPLY_COD_ERROR
                else:
                    num_tentativas += 1

    def __send(self, operacao, a, b):
        operation_server_addr = self.__request_operation_server_addr(operacao.value)

        if operation_server_addr == constantes.NO_SERVER_NAME_REPLY_COD_ERROR:
            return constantes.NO_SERVER_NAME_REPLY_MSG_ERROR
        elif operation_server_addr == constantes.NO_COMPATIBLE_SERVER_COD_ERROR:
            return constantes.NO_COMPATIBLE_SERVER_MSG_ERROR
        else:
            list_server = []
            operation_server_addr_json = json.loads(operation_server_addr)

            for i in operation_server_addr_json:
                list_server.append((i['host'], i['port']))

            return self.__send_to_operation_server(operacao.value, a, b, list_server)

    def soma(self, a, b):
        return self.__send(constantes.Operacoes.SOMA, a, b)

    def subtracao(self, a, b):
        return self.__send(constantes.Operacoes.SUBTRACAO, a, b)

    def multiplicacao(self, a, b):
        return self.__send(constantes.Operacoes.MULTIPLICACAO, a, b)

    def divisao(self, a, b):
        return self.__send(constantes.Operacoes.DIVISAO, a, b)

    def close(self):
        if self.__socket is not None:
            self.__socket.close()
