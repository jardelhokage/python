nota1 = int(input("Primeira Nota: "))
nota2 = int(input("Segunda Nota: "))
nota3 = int(input("Terceira Nota: "))
nota4 = int(input("Quarta Nota: "))
media = [nota1,nota2,nota3,nota4]
soma = sum(media)
print("Nota 1: {} Nota 2: {} Nota 3: {} Nota 4: {}".format(nota1, nota2, nota3, nota4))
print("Média: {}".format(soma/4))
