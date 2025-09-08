n1 = input("ingrese primer numero ")
n2 = input("ingrese segundo numero ")

n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
mensaje = f"""
para los numeros {n1} y {n2}
los resultados de la suma es {suma}
los resultados de la resta es {resta}
los resultados de la division es {division}
los resultados de la multiplicacion es {multiplicacion}"""

print(mensaje)
