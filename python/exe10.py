

salario = float(input("Digite o Valor do seu salário: "))
if(salario == 280):
    aumento = 20
    print("Salário antigo: R${}".format(salario))
    print("Percentual de aumento: {}%".format(aumento)) 
    resultado = salario +(salario*aumento/100)
    valorAumento = resultado - salario
    print("Valor do aumento: R$ {}".format(valorAumento))
    print("Novo salário: R$ {}".format(resultado))
elif(salario > 280 and salario < 700):
    aumento = 15
    print("Salário antigo: R${}".format(salario))
    print("Percentual de aumento: {}%".format(aumento)) 
    resultado = salario +(salario*aumento/100)
    valorAumento = resultado - salario
    print("Valor do aumento: R$ {}".format(valorAumento))
    print("Novo salário: R$ {}".format(resultado))
elif(salario > 700 and salario < 1500):
    aumento = 10
    print("Salário antigo: R${}".format(salario))
    print("Percentual de aumento: {}%".format(aumento)) 
    resultado = salario +(salario*aumento/100)
    valorAumento = resultado - salario
    print("Valor do aumento: R$ {}".format(valorAumento))
    print("Novo salário: R$ {}".format(resultado))
elif(salario >= 1500):
    aumento = 5
    print("Salário antigo: R${}".format(salario))
    print("Percentual de aumento: {}%".format(aumento)) 
    resultado = salario +(salario*aumento/100)
    valorAumento = resultado - salario
    print("Valor do aumento: R$ {}".format(valorAumento))
    print("Novo salário: R$ {}".format(resultado))
    
    
