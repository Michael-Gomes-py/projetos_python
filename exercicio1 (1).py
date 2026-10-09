nome = (input("digite seu nome: "))
arquivo = open ("dados.txt", "w")
arquivo.write (nome + "\n curso : Técnico de Redes \n Turma: 4RM \n")
arquivo.close()