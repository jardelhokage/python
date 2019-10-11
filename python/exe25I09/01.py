primeira = []
segunda =  []

while True:
    e = int(input("primeira lista (0 para terminar):"))
    if e == 0:
        break
    primeira.append(e)

while True:
    e = int(input("segunda lista (0 para terminar):"))
    if e == 0:
        break
    segunda.append(e)
terceira = primeira[:]
terceira.extend(segunda)
x=0
while x < len(terceira):
    print("%d: %d" % (x,  terceira[x]))
    x=x+1

y = 0 
x = y+1 

while True:
    if terceira[y] == terceira[x]:
        del terceira[x] 
    else:
        x += 1 
    if x >= len(terceira):
        y += 1 
        x = y+1 
        if y >= len(terceira)-1: 
            break

quarta = terceira[:]
print(quarta)

