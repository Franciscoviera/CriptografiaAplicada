import hashlib

def calcularHashSHA256(texto):
    # Convierto el texto a bytes con encode(), calculo el hash SHA-256 y lo paso a hexadecimal
    return hashlib.sha256(texto.encode()).hexdigest()


textoOriginal = "Juro solemnemente que mis intenciones no son buenas"

variante1 = "Juro solemnemente que mis intenciones no son buenas."
variante2 = "Juro solemnemente que mis intenciones no son Buenas"
variante3 = "juro solemnemente que mis intenciones no son buenas"
variante4 = "Juro solemnemente que mis intenciones no son malas"

hashOriginal = calcularHashSHA256(textoOriginal)
hashVariante1 = calcularHashSHA256(variante1)
hashVariante2 = calcularHashSHA256(variante2)
hashVariante3 = calcularHashSHA256(variante3)
hashVariante4 = calcularHashSHA256(variante4)

print("Ejercicio 4 Verificacion de integridad con SHA-256")
print()
print("Original: ", textoOriginal)
print("Hash: ", hashOriginal)
print()
print("Variante 1: ", variante1)
print("Hash: ", hashVariante1)
print()
print("Variante 2: ", variante2)
print("Hash: ", hashVariante2)
print()
print("Variante 3: ", variante3)
print("Hash: ", hashVariante3)
print()
print("Variante 4: ", variante4)
print("Hash: ", hashVariante4)
print()

# e)
textoUsuario = input("Ingresa un texto para calcular su SHA-256: ")
print("Hash SHA-256: ", calcularHashSHA256(textoUsuario))