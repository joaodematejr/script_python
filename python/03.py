class Calculadora:
    def calcular(self, numero1, numero2):
        soma = numero1 + numero2
        subtracao = numero1 - numero2
        multiplicacao = numero2 * numero1
        divisao = numero2 / numero1
        print("A soma é:", soma)
        print("A Subtracao é:", subtracao)
        print("A Multiplicacao é:", multiplicacao)
        print("A Divisao é:", divisao)


calcular = Calculadora()

print('Digite o número 1')
numero1 = int(input())

print('Digite o número 2')
numero2 = int(input())

calcular.calcular(numero1, numero2)
