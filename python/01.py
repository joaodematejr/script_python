class Pessoa:
    def validar_idade(self, nome, idade):
        if idade > 18:
            print(nome + " é maior de idade")
        else:
            print(nome + "O aluno é menor de idade")

#Cálculo de média
class Media:
    def media_final(self, n1, n2, n3):
        media = (n1+n2+n3)/3
        if media >= 7:
            print("Sua média foi de %.2f e ele está APROVADO!" %media)
        else:
            print("Sua média foi de %.2f e ele está REPROVADO!" %media)

quantidade_alunos = 5

while quantidade_alunos != 0:
    nome = str (input("\nNome do aluno: "))
    idade = int (input("Digite a idade do aluno: "))
    n1 = float (input("Digite a primeira nota: "))
    n2 = float (input("Digite a segunda nota: "))
    n3 = float (input("Digite a terceira nota: "))
    quantidade_alunos = quantidade_alunos-1
    print("\n")
    maioridade = Pessoa()
    maioridade.validar_idade(nome, idade)
    media = Media()
    media.media_final(n1,n2,n3)
print ("Programa encerrado!")
