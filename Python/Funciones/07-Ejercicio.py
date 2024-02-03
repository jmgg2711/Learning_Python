def Espacios(texto):
    no_espacios = ""
    for _ in texto:
        if _ != " ":
            no_espacios += _
    return no_espacios


def InvertirCadena(texto):
    longitudCadena = 0
    textoInvertido = ""
    for _ in texto:
        longitudCadena += 1
    while longitudCadena > 0:
        longitudCadena -= 1
        textoInvertido += texto[longitudCadena]
    return textoInvertido


# def reverse(texto):
#     texto_al_reves = ""
#     for char in texto:
#         texto_al_reves = char + texto_al_reves
#     return texto_al_reves


def EsPalindromo(texto):
    textoIni = Espacios(texto)
    textoInv = InvertirCadena(textoIni)
    if textoIni.lower() == textoInv.lower():
        return True
    else:
        return False


print("Hola", reverse("Hola"))


print("Abba", EsPalindromo("Abba"))
print("Reconocer", EsPalindromo("Reconocer"))
print("Amo la paloma", EsPalindromo("Amo la paloma"))
print("Hola Mundo", EsPalindromo("Hola Mundo"))
print("Amad a la dama", EsPalindromo("Amad a la dama"))
print("Ana lleva al oso la avellana", EsPalindromo("Ana lleva al oso la avellana"))
print("Acaso hubo buhos aca", EsPalindromo("Acaso hubo buhos aca"))
