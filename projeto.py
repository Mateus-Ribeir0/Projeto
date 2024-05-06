import os
import time
os.system('cls')

def menu_interativo(acao):
    if acao == 1:
        return cadastar_receita()
    elif acao == 2:
        return visualizar()
    elif acao == 3:
        return atualizar()
    elif acao == 4:
        return excluir()
    elif acao == 5:
        return filtragem()
    elif acao == 0:
        return 'PROGRAMA ENCERRADO'
    else:
        return 'Ação inválida'
            
def cadastar_receita():
    os.system('cls')
    file = open('Repositorio_de_receitas.txt', 'a', encoding='utf8')

    formatador = []
    titulo = '''
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█
█▄▄ █▀█ █▄▀ █▀█ ▄█  █  █▀▄ █▄█   █▄▀ ██▄   █▀▄ ██▄ █▄▄ ██▄ █  █  █▀█
'''
    print(titulo)
    nome = str(input("Nome do prato: "))
    formatador.append(nome)

    print("==========================")
    pais = str(input("País de origem: "))
    formatador.append(pais)

    print("==========================")
    i = []
    quant_i = int(input("Quantidade de ingredientes: "))
    for j in range (quant_i):
        ingrediente = str(input(f"Digite o {j+1}° Ingrediente: ").strip())
        i.append(ingrediente)
    i1 = "|".join(i)
    formatador.append(i1)

    print("==========================")
    m = []
    quant_m = int(input("Quantidade de passos: "))
    for i in range (quant_m):
        modo = str(input(f"Digite o {i+1}° passo: ").strip())
        m.append(modo)
    m1 = "|".join(m)
    formatador.append(m1)

    nova_receita = '\n' + ' - '.join(formatador) + ' - False'
    file.write(nova_receita)

    file.close()

def visualizar():


    return 'teste2'

def atualizar():


    return 'teste3'

import os
import time

def excluir():

    os.system('cls')

    file_path = 'Repositorio_de_receitas.txt'
    
    titulo = '''
█▀▀ ▀▄▀ █▀▀ █   █ █ █▀ ▄▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█ █▀
██▄ █ █ █▄▄ █▄▄ █▄█ ▄█ █▀█ █▄█   █▄▀ ██▄   █▀▄ ██▄ █▄▄ ██▄ █  █  █▀█ ▄█
'''

    print(titulo)
    
    receita_excluir = input("Digite o nome da receita que deseja excluir: ").strip().lower()

    with open(file_path, 'r', encoding='utf8') as file:
        todas_as_linhas = file.readlines()
    
    receitas_da_lista = [linha.split(' - ')[0].strip().lower() for linha in todas_as_linhas if linha.strip()]
    
    if receita_excluir not in receitas_da_lista:
        print(f"Receita '{receita_excluir}' não encontrada.")
        time.sleep(2)
        return
    

    linhas_final = [
        linha for linha in todas_as_linhas 
        if linha.strip() and linha.split(' - ')[0].strip().lower() != receita_excluir
    ]
    
    with open(file_path, 'w', encoding='utf8') as file:
        file.writelines(linhas_final)
    
    print(f"Receita '{receita_excluir}' excluída com sucesso.")
    time.sleep(2)


def filtragem():
    os.system('cls')

    file = open('Repositorio_de_receitas.txt', 'r', encoding='utf8')
    lista_de_paises = file.readlines()
    file.close()
    titulo = '''

█▀▀ █ █   ▀█▀ █▀█ █▀█   █▀█ █▀█ █▀█   █▀█ ▄▀█ █ █▀
█▀  █ █▄▄  █  █▀▄ █▄█   █▀▀ █▄█ █▀▄   █▀▀ █▀█ █ ▄█
'''

    print(titulo)
    paises = []
    i = 1
    for receita in lista_de_paises:  # Filtrando os paises em uma lista
        linha = receita.split(' - ')
        paises.append(linha[1])

        if paises.count(linha[1]) == 1:
            print(f"{i} - {linha[1]}")
            i += 1
        else:
            paises.pop()
            continue
    print("==========================================================")
    pais_filtrato = int(input("Escolha o país o qual deseja visualizar as receitas: "))

    os.system('cls')

    receitas_filtradas = []
    for receita in lista_de_paises:  # Separando as receitas do país escolhido em uma lista
        if paises[pais_filtrato - 1] in receita:
            receitas_filtradas.append(receita)
        else:
            continue

    print(f"\t\tReceitas do(a) {paises[pais_filtrato - 1]}  ")
    print("==========================================================")

    nomes_das_receitas = []
    j = 1
    for receita in receitas_filtradas:  # filtrando os nomes das receitas em uma lista para posterior escolha
        nome = receita.split(' - ')
        nomes_das_receitas.append(nome[0])

        print(f"{j} - {nome[0]}")
        j += 1
    print("==========================================================")
    indice_receita_escolhida = int(input("Receita: "))

    receita_escolhida = []
    receita_escolhida_passos = []
    for receita in receitas_filtradas:  # adicionando a receita escolhida em uma lista
        if nomes_das_receitas[indice_receita_escolhida - 1] in receita:
            receita_separada = receita.split(' - ')

            for k in receita_separada:  # formatando os nomes para uma melhor leitura
                if '|' in k and len(k) >= 2:
                    nome_separado = k.split('|')
                    nome_junto = '\n⚬ '.join(nome_separado)
                    nome_junto_passos = '\n☛ '.join(nome_separado)
                    receita_escolhida.append(nome_junto)
                    receita_escolhida_passos.append(nome_junto_passos)
                else:
                    receita_escolhida.append(k)
                    receita_escolhida_passos.append(k)

    os.system('cls')

    print(f"\t\t   ♨  Receita {receita_escolhida[0]}  ♨")
    print("==========================================================")
    print(f"Ingredientes:\n\n⚬ {receita_escolhida[2]}\n")
    print(f"Modo de preparo:\n\n☛  {receita_escolhida_passos[3]}")
    print("==========================================================")

    voltar = str(input("Aperte qualquer tecla para voltar ao menu principal: "))
    

#============ MENU PRINCIPAL ============#

while True:
    os.system('cls')
    titulo = '''

███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝
'''
    print(f"{titulo}\n")

    print("1 - Cadastrar receitas")
    print("2 - Visualizar receitas ")
    print("3 - Atualizar receitas")
    print("4 - Excluir receita")
    print("5 - Filtragem por País")
    print("0 - Sair do programa")
    acao = int(input("\nDigite qual ação deseja realizar: "))

    print(menu_interativo(acao)) # roda/printa a função escolhida

    if acao == 0:
        break
    
#=========================================#