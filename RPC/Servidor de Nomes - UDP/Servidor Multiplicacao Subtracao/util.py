import hashlib
import constantes

def set_format(msg):
    return constantes.DEFAULT_FORMAT % (str(msg), to_hash(str(msg)))

def set_server_operacao_format(operacao, a, b):
    msg = constantes.SERVER_OPERATION_FORMAT % (operacao, str(a), str(b))
    return set_format(msg)

def to_hash(msg):

    md5 = hashlib.md5()
    md5.update(str(msg).encode())

    return md5.hexdigest()

def get_format(msg):
    try:
        msg = msg.split(constantes.SEPARATOR)
    except IndexError:
        return None

    if (to_hash(msg[0]) != msg[1]):
        return None

    return str(msg[0])

def get_server_operacao_format(msg):
    try:
        msg = get_format(msg).split(constantes.OPERATION_SEPARATOR)

        operandos = msg[1].split(constantes.VALUES_OPERATION_SEPARATOR)

    except IndexError:
        return None

    return (msg[0], float(operandos[0]), float(operandos[1]))
