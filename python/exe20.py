count = 0
resp = str(input("Telefonou para a vítima?"))
resp.lower() 
if resp == "sim" or resp == "s":
    
    count = count + 1
    resp = str(input("Esteve no local do crime?"))
    resp.lower() 
if resp == "sim" or resp == "s":
    count = count + 1 
    resp = str(input("Mora perto da vítima?"))
    resp.lower() 
if resp == "sim" or resp == "s":
    count = count + 1 
    resp = str(input("Devia para a vítima?"))
    resp.lower() 
if resp == "sim" or resp == "s":
    count = count + 1 
    resp = str(input("Já trabalhou com a vítima?"))
    resp.lower() 
if resp == "sim" or resp == "s":
    count = count + 1 
if count == 2:
    print("Suspeita(0)")
if count == 3 or count == 4:
    print("Cúmplice")
if count == 5:
    print("Assassino")
else:
    print("Inocente")
