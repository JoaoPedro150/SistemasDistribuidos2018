import json
import util
import constantes
import datetime
import random
from servidor_udp import Servidor

class ServidorNomes(Servidor):

    def __init__(self, port):
        super(ServidorNomes, self).__init__(port)

        with open(constantes.SERVERS_OPERATION_FILE, 'r') as arq:
            self.__servers = json.loads(arq.read())

        print('\nATENÇÃO\nO servidor de nomes não garante e nem verifica se ' +
              'os servidores de operacão estão online.\n\n')

    def novaRequisicao(self, data, client_address):

        msg = util.get_format(data.decode())

        if (msg == None):
            return

        operacao = None

        try:
            print('Enviando os endereços de servidores de %s conhecidos para %s na porta %d...' %
                (constantes.Operacoes(int(msg)).name, client_address[0], client_address[1]))

            operacao = self.__servers[constantes.Operacoes(int(msg)).name.lower()]

            dados = None

            if (len(operacao) == 0):
                dados = constantes.NO_COMPATIBLE_SERVER_COD_ERROR
            else:
                dados = json.dumps(operacao)

        except KeyError:
            dados = constantes.NO_COMPATIBLE_SERVER_COD_ERROR

        status = 'FAIL'

        if random.choice([True, False]):
            self.send(util.set_format(dados), client_address)
            status = 'OK'

        print(status + '. (' + str(datetime.datetime.now()) + ')')

if __name__ == '__main__':
    ServidorNomes(constantes.SERVER_PORT).start()
