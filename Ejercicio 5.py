abc = "abcdefghijklmnopqrstuvwxyz"  # uso el abecedario como vector
def cifrarCesar (texto, desplazamiento):
    resultado = ""
    for caracter in texto.lower():  # paso todo a minuscula
        if caracter in abc:
            pos = abc.index(caracter)  # saco la posicion del caracter
            resultado += abc[(pos + desplazamiento) % 26]    # guardo esa posicion desplazada y verifico q no se pase de 26
        else:
            resultado += caracter  # si no es letra lo dejo igual
    return resultado

def descifrarCesar (cifrado, desplazamiento):
    return cifrarCesar(cifrado, -desplazamiento)

def fuerzaBruta (cifrado):
    print("Fuerza bruta")
    for desplazamiento in range(1,26):
        resultado = descifrarCesar(cifrado, desplazamiento)
        print("Desplazamiento: ", desplazamiento, "   Texto Descifrado", resultado)

print("Ejercicio 5 Cifrado Cesar")
print("a) cifrar un texto dado con un desplazamiento elegido por el usuario")
msjOriginal = input("Ingrese el mensaje que desea cifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
msjCifrado = cifrarCesar(msjOriginal,desplazamiento)
print("Mensaje Cifrado: ", msjCifrado)
msjDescifrado = descifrarCesar(msjCifrado, desplazamiento)
print("Mensaje Descifrado: ", msjDescifrado)

print("b) descifrar un texto dado con un desplazamiento elegido por el usuario")
msjCifrado = input("Ingrese el mensaje que desea descifrar: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))
msjOriginal = descifrarCesar(msjCifrado,desplazamiento)
print("Mensaje Original: ", msjOriginal)

print("c) probar automáticamente todos los desplazamientos posibles del 1 al 25 sobre VOGVCCZRIDLJ:")
fuerzaBruta("VOGVCCZRIDLJ")



