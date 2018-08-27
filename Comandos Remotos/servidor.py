#coding: utf-8

from threading import Thread
import shell

import socket
import threading

DEFALUT_PORT = 12345

def main():

    port = set_port()

    if not port: return 0

    Server(port).start()

    return 0

def set_port():
    port = input('PORT[%d]: ' % DEFALUT_PORT)
    print()

    if (port == ''):
        port = DEFALUT_PORT
    else:
        try:
            port = int(port)
        except ValueError:
            print ('Porta inválida.')
            return

    return port

class Server:

    def __init__(self, port):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(('', port))
        self.__socket.listen(5)

        self.__connections = []
        self.__lock = threading.Lock()


    def start(self):
        try:
            Thread(target=self.__accept, args=()).start()

            print('\nO shell remoto está aceitando conexões.\nPara finalizar digite "exit" ou use "Ctrl+C"\n\n')

            exit_flag = input()

            while (exit_flag != 'exit'):
                exit_flag = input()
        except KeyboardInterrupt:
            pass
        finally:
            self.close()

    def __accept(self):
        while(True):
            connection, client = self.__socket.accept()
            Thread(target=self.newConnection, args=(connection, client)).start()

    def newConnection(self, connection, client):
        import os

        try:
            directory = os.getcwd() + '/'

            print ('Conectado com %s na porta %d ' % client)

            with self.__lock:
                self.__connections.append(connection)

            while (True):
                command = connection.recv(16384).decode()

                if (command == '_exit'): break

                if (command == '_start'):
                    connection.send((socket.gethostname() + ':' + directory).encode())
                    continue

                output = None
                erro = None

                output, erro, directory  = shell.executar_comando(command, directory)

                if (erro):
                    self.__send(erro.decode(), connection, directory)
                elif (output):
                    self.__send(output.decode(), connection, directory)
                else:
                    self.__send(' ', connection, directory)
        finally:
            with self.__lock:
                self.__connections.remove(connection)
                print ('Finalizando conexao com o cliente %s na porta %d  ' % connection.getpeername())
                connection.close()

    @staticmethod
    def __send(data, socket_, directory):
        socket_.send(('%s:%s[-.x.-]%s' % (socket.gethostname(), directory, data)).encode())

    def close(self):
        if (self.__socket):
            if (len(self.__connections) > 0):
                with self.__lock:
                    print('\nEncerrando conexoes...\n')
                    for connection in self.__connections:
                        print ('Finalizando conexao com o cliente %s na porta %d  ' % connection.getpeername())
                        connection.close()
            self.__socket.close()
        print()

if __name__ == "__main__":
    import os
    os._exit(main())
