import cliente_rpc

HOST = '127.0.0.1'
PORT = 12346
cliente = cliente_rpc.Cliente(HOST, PORT)

def soma(a, b):
    return cliente.soma(a, b)

def subtracao(a, b):
    return cliente.subtracao(a, b)

def divisao(a, b):
    return cliente.divisao(a, b)

def multiplicacao(a, b):
    return cliente.multiplicacao(a, b)

def close():
    cliente.close()
