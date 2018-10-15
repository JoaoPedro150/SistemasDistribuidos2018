import cliente_rpc
import constantes

client = cliente_rpc.Cliente(constantes.SERVER_NAME_HOST, constantes.SERVER_NAME_PORT)

def soma(a, b):
    return client.soma(a, b)

def subtracao(a, b):
    return client.subtracao(a, b)

def divisao(a, b):
    return client.divisao(a, b)

def multiplicacao(a, b):
    return client.multiplicacao(a, b)

def close():
    client.close()
