import hashlib

def to_server_format(msg):
    return '%s#%s' % (msg, to_hash(msg))

def to_client_format(operacao, a, b):
    msg = '%s,%s;%s' % (operacao, str(a), str(b))
    return to_server_format(msg)

def to_hash(msg):

    md5 = hashlib.md5()
    md5.update(str(msg).encode())

    return md5.hexdigest()

def get_client_data(msg):
    try:
        msg = msg.split('#')
    except IndexError:
        return None

    if (to_hash(msg[0]) != msg[1]):
        return None

    return msg[0]

def get_server_data(msg):
    try:
        msg = get_client_data(msg).split(',')

        operandos = msg[1].split(';')

    except IndexError:
        return None

    return (msg[0], float(operandos[0]), float(operandos[1]))
