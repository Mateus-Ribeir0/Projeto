import os
os.system('cls')

lista = ['carlos', 'mateus', 'amanda', 'malu', 'joao']

for nome in lista:
    if nome != 'joao':
        print(f"{nome} Aceito")
    else:
        print(f"{nome} Negado")
