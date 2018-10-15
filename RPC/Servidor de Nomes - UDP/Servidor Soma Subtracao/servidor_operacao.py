import util
import constantes
import datetime
import random
from servidor_udp import Servidor
from abc import abstractmethod

class ServidorOperacao(Servidor):
    def novaRequisicao(self, data, client_address):

        msg = util.get_server_operacao_format(data.decode())

        if (msg == None):
            return

        operacao = constantes.Operacoes(int(msg[0]))

        print('Efetuando %s solicitada por %s na porta %d...' % (operacao.name, client_address[0], client_address[1]))

        status = 'FAIL'

        if random.choice([True, False]):
        	self.send(util.set_format(self.operacao(operacao, msg[1], msg[2])), client_address)
       		status = 'OK'

       	print(status + '. (' + str(datetime.datetime.now()) + ')')
       

    @abstractmethod
    def operacao(operacao, num1, num2):
        pass
