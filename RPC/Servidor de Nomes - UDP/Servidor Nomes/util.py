import hashlib
import constantes

def set_format(msg):
    return constantes.DEFAULT_FORMAT % (str(msg), to_hash(str(msg)))

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
