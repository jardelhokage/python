v = [x for x in range(1,7)]
produto = 1
for x in v:
  produto *= x
print("Soma dos elementos:",sum(v))
print("Produto dos elementos:",produto)
print("Números:",end=" ")
for x in v:
  print(x,end=" ")
