#coding: utf-8

import socket
import threading
import shell

from threading import Thread

DEFALUT_HOST = '127.0.0.1'
DEFALUT_PORT = 12345

def main():
    host, port = set_server_address()

    if not host:
        return 0

    try:
        Client().start(host, port)

    except ConnectionRefusedError:
        print('Conexão recusada.')

    return 0

def set_server_address():
    host = input('HOST[%s]: ' % DEFALUT_HOST)
    port = input('PORT[%d]: ' % DEFALUT_PORT)
    print()

    if (host == ''):
        host = DEFALUT_HOST

    if (port == ''):
        port = DEFALUT_PORT
    else:
        try:
            port = int(port)
        except ValueError:
            print ('Porta inválida.')
            return None, None

    return host, port

class Client:

    def __init__(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__lock = threading.Condition()
        self.__reply = None
        self.__mode = 'remote'
        self.__directory = None

    def start(self, host, port):
        self.__socket.connect((host,port))
        print('Conexão estabelecida com o servidor %s na porta %d.\nUse "_exit" para encerrar a conexão ou "Ctrl+C".\n\n' % (host,port))

        self.__lock.acquire()
        Thread(target=self.__send_comand, args=()).start()

        self.__get_reply()
        print()

    def __recv(self):
        if (self.__mode == 'local'):
            self.__lock.acquire()
            self.__lock.wait()
            self.__lock.release()

            output = None
            erro = None

            output, erro, self.__directory  = shell.executar_comando(self.__reply, self.__directory)

            if (erro):
                return ('%s:%s[-.x.-]%s' % (socket.gethostname(), self.__directory, erro.decode()))
            elif (output):
                return ('%s:%s[-.x.-]%s' % (socket.gethostname(), self.__directory, output.decode()))
            else:
                return ('%s:%s[-.x.-] ' % (socket.gethostname(), self.__directory))
        else:
            return self.__socket.recv(16384).decode()

    def __get_reply(self):
        try:
            self.__socket.send('_start'.encode())
            output = self.__socket.recv(16384).decode()

            self.__reply = output[:-1] + '$ '

            self.__lock.release()

            while(True):
                output = self.__recv()

                if not output:
                    if (self.__mode == 'end'):
                        break
                    else:
                        import os

                        self.__close()
                        self.__mode = 'local'
                        self.__directory = os.getcwd() + '/'

                        print('\n\nConexão perdida.\nAlternando para o modo de execução local.\n')

                        print ('%s:%s$ ' % (socket.gethostname(), self.__directory[:-1] + '$ '))

                        continue

                output = output.split('[-.x.-]')

                print('\n' + output[1])

                self.__reply = output[0][:-1] + '$ '

                self.__lock.acquire()
                self.__lock.notify()
                self.__lock.release()

        except KeyboardInterrupt:
            if (self.__mode != 'local'):
                self.__socket.send('_exit'.encode())
        finally:
            self.__close()

    def __send_comand(self):
        try:
            self.__lock.acquire()

            comando = input(self.__reply)

            self.__lock.release()

            while (comando != '_exit'):

                if (comando == 'clear'):
                    import os
                    os.system('clear')

                elif(comando != ''):
                    self.__send(comando)

                    self.__lock.acquire()
                    self.__lock.wait()
                    self.__lock.release()

                comando = input(self.__reply)

            self.__socket.send(comando.encode())
            self.__mode = 'end'

        except KeyboardInterrupt:
            pass

    def __send(self, comando):
        if (self.__mode == 'local'):
            self.__reply = comando
            self.__lock.acquire()
            self.__lock.notify()
            self.__lock.release()
        else:
            self.__socket.send(comando.encode())

    def __close(self):
        if (self.__mode != 'local'):
            self.__socket.close()

if __name__ == "__main__":
    import os
    os._exit(main())
