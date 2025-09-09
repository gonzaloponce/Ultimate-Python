# and, or, not

gas = True
encendido = True

if gas and encendido:
    print("Puedes Avanzar")

gas = True
encendido = False
if gas and encendido:
    print("Puedes Avanzar")

if gas or encendido:
    print("Puedes Avanzar")


gas = False
encendido = True
edad = 18
if not gas and encendido and edad > 17:
    print("Puedes Avanzar")
