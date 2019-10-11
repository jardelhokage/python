vogais = ['a', 'e', 'i', 'o', 'u']
letra = input("Digite uma letra: ")
if(letra in vogais):
  print("Vogal")
elif letra.isalpha():
  print("Consoante")
else:
  print("Não é uma letra")
