
class Validar:
    def validar_numero(self, numero1):
        if numero1 >= 0:
            #validação de pares
            if numero1 % 2 == 0:
                print ("O número é positivo e par")
            else:
                print ("O número é positivo e ímpar")
        else:
            #validação de impares
            if numero1 % 2 == 0:
                print ("O número é negativo e par")
            else:
                print ("O número é negativo e ímpar")

validar = Validar()
numero = int(input("Digite um numero: "))

validar.validar_numero(numero)
