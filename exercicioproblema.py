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
    arquivo.close()

    hash_calculado = hashlib.sha256(conteudo).hexdigest()

    print("Arquivo:", arquivo_selecionado)
    print("SHA-256 Calculado:", hash_calculado)
    print("-" * 100)

    hash_original = input("Digite o SHA-256 fornecido pela TI: ")

    if hash_calculado.lower() == hash_original.strip().lower():
        print("\nSituação: O arquivo está ÍNTEGRO!")
    else:
        print("\nSituação: O arquivo está CORROMPIDO ou foi ALTERADO!")

else:
    print("Nenhum arquivo foi selecionado.")