import socket
import constantes

from abc import ABC, abstractmethod

class Servidor(ABC):

    def __init__(self, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(('',port))

    def start(self):
        try:
            while True:
                data, client_address = self.__socket.recvfrom(constantes.BUFFER_SIZE)
                self.novaRequisicao(data, client_address)
        except KeyboardInterrupt:
            print()
        finally:
            self.close()

    @abstractmethod
    def novaRequisicao(self, data, client_address):
        pass

    def send(self, msg, address):
        self.__socket.sendto(str(msg).encode(), (address))

    def close(self):
        if self.__socket is not None:
            self.__socket.close()
