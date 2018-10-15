from enum import Enum

Operacoes = Enum('Operacoes', ['SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO'])

# Formato das mensagens utilizadas
DEFAULT_FORMAT = '%s#%s'
SERVER_OPERATION_FORMAT = '%s,%s;%s'
SEPARATOR = '#'
OPERATION_SEPARATOR = ','
VALUES_OPERATION_SEPARATOR = ';'

# Tamanho do buffer de resposta
BUFFER_SIZE = 1024

# Porta utilizada
SERVER_PORT = 12349
