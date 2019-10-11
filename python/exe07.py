primeiro = int(input('Primeiro Produto: '))
segundo = int(input('Segundo Produto : '))
terceiro = int(input('Terceiro Produto: '))
maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('Vc deve comprar esse produto: ',menor)
