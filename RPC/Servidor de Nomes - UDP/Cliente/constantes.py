import json
from enum import Enum

Operacoes = Enum('Operacoes', ['SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO'])

# Formato das mensagens utilizadas pela aplicacao
DEFAULT_FORMAT = '%s#%s'
SERVER_OPERATION_FORMAT = '%s,%s;%s'
SEPARATOR = '#'
OPERATION_SEPARATOR = ','
VALUES_OPERATION_SEPARATOR = ';'

# Constantes de erro
NO_SERVER_OPERATION_REPLY_MSG_ERROR = 'Nenhum servidor de operação respondeu a solicitação.'
NO_SERVER_NAME_REPLY_MSG_ERROR = 'O servidor de nomes não respondeu a solicitação.'
NO_COMPATIBLE_SERVER_MSG_ERROR = 'Não há nenhum servidor disponível para esta operação.'

# Constantes de erro
NO_SERVER_NAME_REPLY_COD_ERROR = '1'
NO_COMPATIBLE_SERVER_COD_ERROR = '2'

# Tempo máximo de espera por resposta
TIME_OUT = 0.6

# Número máximo de tentativas de comunicação
MAX_ATTEMPTS = 3

# Tamanho do buffer de resposta
BUFFER_SIZE = 1024

# Servidor de nomes
SERVER_NAME_HOST = '127.0.0.1'
SERVER_NAME_PORT = 12345
