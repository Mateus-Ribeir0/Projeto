<<<<<<< HEAD
print("Commit inicial mudei")
print('carlosss')
=======
print("Commit inicial mcarlsudei")

import os
os.system('cls')

def media(n1, n2):
    media = (n1*1 + n2*2) / 3
    return media

def situacao(media):
    if media > 6:
        return 'Aprovado'
    elif media < 4:
        return 'Reprovado'
    else:
        return 'Verificação suplementar'

n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
md = media(n1, n2)
print(f"A média foi de: {md}\nsituação: {situacao(md)}")
>>>>>>> ba65d7aa503c49eaa63cb9e15a6f9dcf2e40d3e8
