import hashlib

texto ="ola, mundo"

hash_texto = hashlib.sha256(texto.encode()).hexdigest()

print ("texto: ",texto)

print ("sha-256: ",hash_texto)


