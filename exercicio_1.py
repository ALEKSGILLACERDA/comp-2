import os
caminho_arquivo = r"C:\Users\aleks\OneDrive\Área de Trabalho\estudo\comp 2\teste_novo\meu_arquivo.py"
with open(caminho_arquivo, "w") as f:
    f.write('print("arquivo criado com sucesso")')
print("Arquivo criado em:", caminho_arquivo)
