# Escriba un programa para hacer un patrón como un triángulo rectángulo con el número aumentado en 1.
# El patrón como:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n=int(input("Ingrese un número "))
numero = 1
for i in range(1,n+1):
    fila = ""
    for j in range(1,i+1):
        fila += str(numero)+ " "
        numero += 1
    print(fila)


