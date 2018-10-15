import constantes
from servidor_operacao import ServidorOperacao

class ServidorDivisaoSoma(ServidorOperacao):
    def operacao(self, operacao, num1, num2):

        if (operacao == constantes.Operacoes.SOMA):
            return num1 + num2
        elif (operacao == constantes.Operacoes.DIVISAO):
            if (num2 == 0):
                return constantes.DIVISION_BY_0
            else:
                return num1 / num2

if __name__ == '__main__':
    ServidorDivisaoSoma(constantes.SERVER_PORT).start()
