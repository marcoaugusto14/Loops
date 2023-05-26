# Escriba un programa para mostrar el patrón como el triángulo de ángulo recto con un asterisco.
# El patrón como:
# *
# **
# *
# ****

n=int(input("Ingrese el número de renglones del triangulo "))
for x in range(n+1):
  print("*"*x)