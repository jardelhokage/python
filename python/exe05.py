notaA = int(input("Digite a primeira nota: "))
notaB = int(input("Digite a segunda nota: "))
media = (notaA + notaB)/2
if(media == 10):
    print("Aprovado com distinção")
elif(media < 7):
    print("Reprovado")
elif(media >= 7):
    print("Aprovado")
    
