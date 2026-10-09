import hashlib 
arquivo=open ("teste.txt","rb")
conteudo=arquivo.read()
hash=hashlib.sha256(conteudo).hexdigest()

print("sha-256: ",hash)

arquivo.close