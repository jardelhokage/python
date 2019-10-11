quantidade = 0
codigo = 0
p = 0
while True:
    n = int(input("Digite o codigo:"))
    a = int(input("Digite a quantidade:"))
    quantidade = a + quantidade
    if n == 1:
        p = p + 0.50
        p = p * a
    if n == 2:
        p = p + 1.00
        p = p * a
    if n == 3:
        p = p + 4.00
        p = p * a
    if n == 5:
        p = p + 7.00
        p = p * a
    if n == 9:
        p = p + 8.00
        p = p * a
    if n == 0 :
        print("Total a pagar:",preco)
    else:
        print("Código inválido")
