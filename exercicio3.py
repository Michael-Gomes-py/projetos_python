import hashlib
import tkinter as tk
from tkinter import filedialog

janela = tk.Tk()
janela.withdraw()

arquivo_selecionado = filedialog.askopenfilename(
title="Selecione um arquivo"
)

if arquivo_selecionado:
    arquivo = open(arquivo_selecionado, "rb")
    conteudo = arquivo.read()
    hash_arquivo = hashlib.sha256(conteudo).hexdigest()

    arquivo.close()

    print("Arquivo:", arquivo_selecionado)
    print("SHA-256:", hash_arquivo)

else:
    print("Nenhum arquivo foi selecionado.")