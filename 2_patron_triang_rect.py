# Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número.
# El patrón como:
# 1
# 12
# 123
# 1234

n=int(input("Ingrese un número "))
if n>0:
  for i in range(1,n+1):
    print("")
    for j in range(1,i+1):
       print(j, end=" ")
else:
  print(" El número ingresad no corresponde")