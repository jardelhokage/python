a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
operacao = input("Digite a operação + , -, *, / : ")
if(operacao == "+"):
    r = a + b
    print("Resultado {}".format(r))
    if(r%2==0):
        print("Valor par")
    else:
        print("Valor impar")
    if(r < 0):
        print("Valor negativo")
    else:
        print("Valor positivo")
    print("Valor int?:",isinstance(r, int))
    print("Valor float?:",isinstance(r, float))
if(operacao == "-"):
    r = a - b
    print("Resultado {}".format(r))
    if(r%2==0):
        print("Valor par")
    else:
        print("Valor impar")
    if(r < 0):
        print("Valor negativo")
    else:
        print("Valor positivo")
    print("Valor int?:",isinstance(r, int))
    print("Valor float?:",isinstance(r, float))
if(operacao == "*"):
    r = a * b
    print("Resultado {}".format(r))
    if(r%2==0):
        print("Valor par")
    else:
        print("Valor impar")
    if(r < 0):
        print("Valor negativo")
    else:
        print("Valor positivo")
    print("Valor int?:",isinstance(r, int))
    print("Valor float?:",isinstance(r, float))
if(operacao == "/"):
    r = a / b
    print("Resultado {}".format(r))
    if(r%2==0):
        print("Valor par")
    else:
        print("Valor impar")
    if(r < 0):
        print("Valor negativo")
    else:
        print("Valor positivo")
    print("Valor int?:",isinstance(r, int))
    print("Valor float?:",isinstance(r, float))
