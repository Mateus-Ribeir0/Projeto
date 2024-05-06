import os
import time
os.system('cls')

def menu_interativo(acao):
    if acao == 'C':
        return cadastar_receita()
    elif acao == 'V':
        return visualizar()
    elif acao == 'R':
        return atualizar()
    elif acao == 'E':
        return excluir()
    elif acao == 'F':
        return filtragem()
    elif acao == 'S':
        return 'PROGRAMA ENCERRADO'
    else:
        return 'Ação inválida'
            
def cadastar_receita():
    os.system('cls')
    file = open('Repositorio_de_receitas.txt', 'a', encoding='utf8')

    formatador = []
    print("   Cadastro de receitas   ")
    print("==========================")
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

    os.system('cls')
    
    print("   Exclusão de receitas   ")
    print("==========================")
    
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

    print("\t\tFiltragem de receitas   ")
    print("==========================================================")

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
    pais_filtrato = int(input("País: "))

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
    for receita in receitas_filtradas:  # adicionando a receita escolhida em uma lista
        if nomes_das_receitas[indice_receita_escolhida - 1] in receita:
            receita_separada = receita.split(' - ')

            for k in receita_separada:  # formatando os nomes para uma melhor leitura
                if '|' in k:
                    nome_separado = k.split('|')
                    nome_junto = '\n• '.join(nome_separado)
                    receita_escolhida.append(nome_junto)
                else:
                    receita_escolhida.append(k)

    os.system('cls')

    print(f"\t\t   Receita {receita_escolhida[0]}")
    print("==========================================================")
    print(f"Ingredientes:\n\n• {receita_escolhida[2]}\n")
    print(f"Modo de preparo:\n\n• {receita_escolhida[3]}")
    print("==========================================================")

    voltar = str(input("Aperte qualquer tecla para voltar: "))
    

#============ MENU PRINCIPAL ============#

while True:
    os.system('cls')
    print("======{ Menu de receitas }======\n")
    print("C - Cadastrar receitas")
    print("V - Visualizar receitas ")
    print("A - Atualizar receitas")
    print("E - Excluir receita")
    print("F - Filtragem por País")
    print("S - Sair do programa")
    acao = str(input("\nAção: ").upper())

    print(menu_interativo(acao)) # roda/printa a função escolhida

    if acao == 'S':
        break
    
#=========================================#