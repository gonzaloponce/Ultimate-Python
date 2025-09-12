def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    indice_inverso = len(texto) - 1

    for letra in texto:
        if letra == texto[indice_inverso]:
            indice_inverso -= 1
        else:
            return False
    return True


palabra = "abba"
print(palabra, es_palindromo(palabra))


palabra = "reconocer"
print(palabra, es_palindromo(palabra))


palabra = "amo la paloma"
print(palabra, es_palindromo(palabra))


palabra = "Hola Mundo"
print(palabra, es_palindromo(palabra))
