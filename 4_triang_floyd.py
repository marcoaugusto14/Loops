# Escriba un programa para imprimir el Triángulo de Floyd.
# 1
# 01
# 101
# 0101
# 10101

n=int(input("Ingrese un número "))
for i in range(1,n+1):
    fila = ""
    for j in range(1,i+1):
        if(i+j) % 2 == 0:
            fila += "1"
        else:
            fila += "0"
    print(fila)
