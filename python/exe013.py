a= int(input('Primeiro lado: '))
b= int(input('Segundo lado: '))
c= int(input('Terceiro lado: '))

if not (a+b)>c and (a+c)>b and (b+c)>a:
   print('\n\nOs lados fornecidos não formam um triângulo\n\n')
elif(a==b and a==c):
   print('\n\nO triângulo é equilátero\n\n')
elif(a!=b and a!=c and b!=c):
   print('\n\nO triângulo é escaleno\n\n')
else:
   print('\n\nO triângulo é isósceles\n\n')
