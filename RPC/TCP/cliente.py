import modulo
import os

def main():
    while True:
        os.system('clear')
        operacao = int(input('1-Soma\n2-Subtração\n3-Divisão\n4-Multiplicação\n5-Sair\n\nEscolha: '))

        if operacao == 5:
            break

        a = float(input('\nNúmero 1: '))
        b = float(input('Número 2: '))
        resultado = '\nResultado: '

        if operacao == 1:
            resultado += modulo.soma(a,b)
        elif operacao == 2:
            resultado += modulo.subtracao(a,b)
        elif operacao == 3:
            resultado += modulo.divisao(a,b)
        elif operacao == 4:
            resultado += modulo.multiplicacao(a,b)
        else:
            print("\nOpção inválida!")
            continue

        print(resultado)
        input('\nPressione enter para continuar...')

    modulo.close()
    return 0

if __name__ == '__main__':
	main()
