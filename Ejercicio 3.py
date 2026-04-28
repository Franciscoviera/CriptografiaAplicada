import hashlib

# Hash esperado del archivo original dado por el enunciado
hashEsperado = "944a1e869969dd8a4b64ca5e6ebc209a"


def calcularHashMD5(arch):
    archivo = open(arch, "rb")
    # Abro el archivo en modo binario para leer los bytes exactos
    # Necesito que este en bytes para usar hashlib.md5
    contenido = archivo.read()
    return hashlib.md5(contenido).hexdigest()  # Calculo el hash MD5 del contenido y lo convierto en hexadecimal


hashFelix1 = calcularHashMD5("potion_felix1.txt")
hashFelix2 = calcularHashMD5("potion_felix2.txt")

print("Ejercicio 3 Hash MD5 de archivos")
print()
print("Hash esperado: ", hashEsperado)
print()
print("potion_felix1.txt Hash MD5: ", hashFelix1)
print("potion_felix2.txt Hash MD5: ", hashFelix2)
print()

if hashFelix1 == hashEsperado:
    print("potion_felix1.txt coincide con el archivo original")
else:
    print("potion_felix1.txt NO coincide con el archivo original")

if hashFelix2 == hashEsperado:
    print("potion_felix2.txt coincide con el archivo original")
else:
    print("potion_felix2.txt NO coincide con el archivo original")