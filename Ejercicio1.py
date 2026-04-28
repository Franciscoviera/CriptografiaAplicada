from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Uso b para cambiar de tipo string a bits
mensaje = b"Expecto Patronum"
clave = b"12345678901234567890123456789012"  # clave de 32 bytes, entonces es AES con clave de 256 bits

# Genera 16 bytes random, uso 16 porq tiene que ser del tamaño del bloque, que usando AES es 16 bytes
vectorInicial = os.urandom(16)

# Como AES usa bloques fijos de 16 bytes, tengo que rellenar cuando no se ocupa todo el bloque
# Si diese para llenar justo todos los bloques igual se agrega un bloque entero de relleno
# para que sepa donde termina el mensaje real
# PKCS7 es el estandar para AES
rellenador = padding.PKCS7(128).padder()
mensajeRelleno = rellenador.update(mensaje) + rellenador.finalize()

# Creo y defino un cifrador AES en modo CBC
cifrador = Cipher(
    algorithms.AES(clave),  # define que algoritmo va a usar y le paso la clave
    modes.CBC(vectorInicial),  # en que modo opera y con que vector inicial (CBC)
    backend=default_backend()
)
# Lo pongo en modo encryptor para cifrar el mensaje ya con relleno
encriptador = cifrador.encryptor()
mensajeCifrado = encriptador.update(mensajeRelleno) + encriptador.finalize()

# Ahora lo pongo en modo decryptor y le paso el mensaje cifrado, me lo devuelve con relleno
desencriptador = cifrador.decryptor()
mensajeDescifradoRelleno = desencriptador.update(mensajeCifrado) + desencriptador.finalize()

# Saco el relleno para recuperar el texto original
sacaRelleno = padding.PKCS7(128).unpadder()
mensajeDescifrado = sacaRelleno.update(mensajeDescifradoRelleno) + sacaRelleno.finalize()

print("Ejercicio 1 - Cifrado AES en modo CBC")
print("Texto plano original: ", mensaje.decode())
print("Clave: ", clave.decode())
print("Vector Inicial: ", vectorInicial.hex())
print("Texto Cifrado: ", mensajeCifrado.hex())
print("Texto Descifrado: ", mensajeDescifrado.decode())
