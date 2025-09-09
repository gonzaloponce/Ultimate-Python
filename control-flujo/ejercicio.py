comandos = ""
num1 = None
while comandos.lower() != "salir":
    if (num1 is None):
        num1 = input("$ Ingrese numero 1: ")
        num1 = int(num1)

    resu = 0

    comandos = input("$ Ingrese operador (sum-res-div-mult): ")
    if (comandos.lower() != "salir"):
        operador = comandos
    else:
        print("salir")
        break

    comandos = input("$ Ingrese Numero 2: ")
    if (comandos.lower() != "salir"):
        num2 = comandos
        num2 = int(num2)
    else:
        print("salir")
        break

    if operador.lower() == "sum":
        resu = num1 + num2
    elif operador.lower() == "rest":
        resu = num1 - num2
    elif operador.lower() == "mult":
        resu = num1 * num2
    elif operador.lower() == "div":
        resu = num1 / num2
    else:
        resu = num1

    print("el resultado es :", resu)
    num1 = resu
