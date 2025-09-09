for numero in range(5):
    print(numero, numero * 'hola mundo ')

buscar = 3
for numero in range(5):
    if numero == buscar:
        print("encontrado: ", buscar)
        break
else:
    print("no encontre el numero: ", buscar)

for char in "ultimate python":
    print(char)
