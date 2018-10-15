from enum import Enum

Operacoes = Enum('Operacoes', ['SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO'])

# Formato das mensagens utilizadas
DEFAULT_FORMAT = '%s#%s'
SEPARATOR = '#'

# Constantes de erro
NO_COMPATIBLE_SERVER_COD_ERROR = 2

# Tamanho do buffer de resposta
BUFFER_SIZE = 1024

# Porta utilizada
SERVER_PORT = 12345

# Path do arquivo com a relação de servidores de operação
SERVERS_OPERATION_FILE = 'lista_servidores.json'
