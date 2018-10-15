import constantes
from servidor_operacao import ServidorOperacao

class ServidorSomaSubtracao(ServidorOperacao):
    def operacao(self, operacao, num1, num2):
        if (operacao == constantes.Operacoes.SOMA):
            return num1 + num2
        elif (operacao == constantes.Operacoes.SUBTRACAO):
            return num1 - num2

if __name__ == '__main__':
    ServidorSomaSubtracao(constantes.SERVER_PORT).start()
