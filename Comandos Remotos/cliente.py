#coding: utf-8

import socket

HOST = '10.3.1.50'
PORT = 14000

def main():
  clienteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server = (HOST, PORT)
  clienteSocket.connect(server)

  comando = raw_input('Comando: ')

  while (True):
    clienteSocket.send(comando.encode())

    output = clienteSocket.recv(2048).decode()
    if not output: break

    print('\n')
    print(output)
    print('\n')

    comando = raw_input('Comando: ')

  clienteSocket.close()

if __name__ == "__main__":
    main()
