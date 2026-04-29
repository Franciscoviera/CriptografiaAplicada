from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Uso b para cambiar de tipo string a bytes
mensaje = b"Expecto Patronum"
clave = b"12345678901234567890123456789012"  # clave de 32 bytes, entonces es AES con clave de 256 bits


def aplicarRelleno(msj):
    # Como AES usa bloques fijos de 16 bytes, tengo que rellenar cuando no se ocupa todo el bloque
    # Si diese para llenar justo todos los bloques igual se agrega un bloque entero de relleno
    # para que sepa donde termina el mensaje real
    rellenador = padding.PKCS7(128).padder()
    return rellenador.update(msj) + rellenador.finalize()


def cifrarMensaje(msj, cla, mod):
    # Aplico relleno al mensaje y creo el cifrador con el algoritmo, modo y backend
    mensajeRelleno = aplicarRelleno(msj)
    cifrador = Cipher(
        algorithms.AES(cla),  # define que algoritmo va a usar y le paso la clave
        mod,                   # en que modo opera (CBC, OFB, CFB o ECB)
        backend=default_backend()
    )
    # Lo pongo en modo encryptor para cifrar el mensaje ya con relleno
    encriptador = cifrador.encryptor()
    return encriptador.update(mensajeRelleno) + encriptador.finalize()


# Genero vectores iniciales random de 16 bytes para CBC, OFB y CFB
# Uso 16 porq tiene que ser del tamaño del bloque, que usando AES es 16 bytes
# ECB no usa vector inicial
vectorInicialCBC = os.urandom(16)
vectorInicialOFB = os.urandom(16)
vectorInicialCFB = os.urandom(16)

# Cifro el mensaje con cada modo pasandole el modo como parametro
mensajeCifradoCBC = cifrarMensaje(mensaje, clave, modes.CBC(vectorInicialCBC))
mensajeCifradoOFB = cifrarMensaje(mensaje, clave, modes.OFB(vectorInicialOFB))
mensajeCifradoCFB = cifrarMensaje(mensaje, clave, modes.CFB(vectorInicialCFB))
mensajeCifradoECB = cifrarMensaje(mensaje, clave, modes.ECB())  # ECB no usa vector inicial

print("Ejercicio 2 Comparacion de modos AES")
print("Mensaje original: ", mensaje.decode())
print("Clave: ", clave.decode())
print()
print("CBC - Vector Inicial: ", vectorInicialCBC.hex())
print("CBC - Texto Cifrado:  ", mensajeCifradoCBC.hex())
print()
print("OFB - Vector Inicial: ", vectorInicialOFB.hex())
print("OFB - Texto Cifrado:  ", mensajeCifradoOFB.hex())
print()
print("CFB - Vector Inicial: ", vectorInicialCFB.hex())
print("CFB - Texto Cifrado:  ", mensajeCifradoCFB.hex())
print()
print("ECB - Sin vector inicial")
print("ECB - Texto Cifrado:  ", mensajeCifradoECB.hex())
