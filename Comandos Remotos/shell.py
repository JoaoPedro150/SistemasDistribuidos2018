import subprocess

def executar_comando(command, directory):

    args = []

    for arg in command.split(' '):
        if(arg != ''):
            args.append(arg)

    if (len(args) == 0):
        return None, None, directory

    if (args[0] == 'cd'):
        return __comando_cd(args, command, directory)
    else:
        try:
            p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory)
            tuple = p.communicate()
            return tuple[0], tuple[1], directory
        except FileNotFoundError:
            return None, (args[0] + ': comando não encontrado').encode(), directory

def __comando_cd(args, command, directory):
    import getpass

    if (len(args) < 2):
        return None, None, '/home/' + getpass.getuser() + '/'

    if (args[1] == '..'):
        return None, None, directory[:-(len(directory) - directory[:-1].rfind('/'))] + '/'

    if (args[1] == '.'):
        return None, None, directory

    if (args[1] == '/'):
        self.__directory = '/'
        return None, None, directory

    args[0] = 'ls'
    output, erro = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory).communicate()

    if not erro:
        directory += args[1] + '/'
    else:
        dir = command[3:]

        output = subprocess.Popen([args[0], dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory).communicate()[0]

        if not output:
            return None, ('cd: "' + dir + '": Arquivo ou diretório inexistente').encode(), directory
        else:
            return None, None, directory + dir + '/'

    return None, erro, directory
