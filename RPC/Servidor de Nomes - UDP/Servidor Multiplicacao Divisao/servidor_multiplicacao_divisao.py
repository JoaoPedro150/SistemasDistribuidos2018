import constantes
from servidor_operacao import ServidorOperacao

class ServidorMultiplicacaoDivisao(ServidorOperacao):
    def operacao(self, operacao, num1, num2):
        if (operacao == constantes.Operacoes.MULTIPLICACAO):
            return num1 * num2
        elif (operacao == constantes.Operacoes.DIVISAO):
            if (num2 == 0):
                return constantes.DIVISION_BY_0
            else:
                return num1 / num2

if __name__ == '__main__':
    ServidorMultiplicacaoDivisao(constantes.SERVER_PORT).start()
