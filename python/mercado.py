vCompra = int(input("Digite o valor de compra: "))
desconto = int(input("Digte o valor do desconto: "))
vPago = int(input("Digite o valor pago: "))
desc = int((desconto/100)*vCompra)
vCompra = vCompra - desc
troco = vPago - vCompra
print("Troco R${}".format(troco))
print("Valor do desconto R${}".format(desc))
print("Valor da compra com desconto R${}".format(vCompra))



,
