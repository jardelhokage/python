turno = input("Em qual turno vc estuda? M para matutino e V para vespertino ou N noturno: ")
if(turno == "M" or turno == "m"):
    print("Bom dia !")
elif (turno == "V" or turno == "v"):
    print("Boa tarde !")
elif (turno == "N" or turno == "n"):
    print("Boa noite !")
else:
    print("Valor não existe !")
