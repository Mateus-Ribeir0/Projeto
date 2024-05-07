import os
import time

def menu_interativo(acao):
    if acao == '1':
        return cadastar_receita()
    elif acao == '2':
        return visualizar_receita()
    elif acao == '3':
        return atualizar()
    elif acao == '4':
        return excluir()
    elif acao == '5':
        return filtragem()
    elif acao == '0':
        return print('===================\nPROGRAMA ENCERRADO\n===================')
    else:
        return print('Ação inválida')
            
def cadastar_receita():
    os.system('cls')
    file = open('Repositorio_de_receitas.txt', 'a', encoding='utf8')

    lista_de_cadastro = []
    titulo = '''
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█
█▄▄ █▀█ █▄▀ █▀█ ▄█  █  █▀▄ █▄█   █▄▀ ██▄   █▀▄ ██▄ █▄▄ ██▄ █  █  █▀█
'''
    print(titulo)
    nome = str(input("Nome do prato: "))
    lista_de_cadastro.append(nome)

    print("==========================")
    pais = str(input("País de origem: ")).capitalize()
    lista_de_cadastro.append(pais)

    print("==========================")
    receita_de_ingredientes = []
    quant_de_ingredientes = int(input("Quantidade de ingredientes: "))
    print("==========================")
    for posicao in range (quant_de_ingredientes):
        ingrediente = str(input(f"Digite o {posicao+1}° Ingrediente: ").strip())
        receita_de_ingredientes.append(ingrediente)
    juncao_ingredientes = " | ".join(receita_de_ingredientes)
    lista_de_cadastro.append(juncao_ingredientes)

    print("==========================")
    passos = []
    quant_de_passos = int(input("Quantidade de passos: "))
    print("==========================")
    for posicao in range (quant_de_passos):
        modo = str(input(f"Digite o {posicao+1}° passo: ").strip())
        passos.append(modo)
    juncao_passos = "|".join(passos)
    lista_de_cadastro.append(juncao_passos)

    nova_receita = '\n' + ' - '.join(lista_de_cadastro) + ' - False'
    file.write(nova_receita)

    file.close()

def obter_receitas():
    os.system('cls')
    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        linhas_arquivo = arquivo.readlines()
    
    receitas = []
    for linha in linhas_arquivo:
        partes = linha.split(' - ')
        receitas.append(partes[0])
    
    return receitas

def selecionar_receita_view(receitas):
    for i, receita in enumerate(receitas, 1):
        print(f"{i:^2} - {receita}")

    print("==========================================================")
    numero = int(input("Digite o número da receita que você quer ver: "))
    return receitas[numero - 1]
def selecionar_receita_edit(receitas):
    for i, receita in enumerate(receitas, 1):
        print(f"{i:^2} - {receita}")

    print("==========================================================")
    numero = int(input("Digite o número da receita que você quer editar: "))
    return receitas[numero - 1]

def exibir_receita(receita):
    receitas_escolhida = []
    receitas_escolhida_passos = []

    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            if receita in linha:
                partes = linha.split(' - ')
                for parte in partes:
                    if '|' in parte and len(parte) >= 2:
                        nomes_separados = parte.split('|')
                        nomes_juntos = '\n⚬ '.join(nomes_separados)
                        nomes_juntos_passos = '\n☛ '.join(nomes_separados)
                        receitas_escolhida.append(nomes_juntos)
                        receitas_escolhida_passos.append(nomes_juntos_passos)
                    else:
                        receitas_escolhida.append(parte)
                        receitas_escolhida_passos.append(parte)

    os.system('cls')

    print(f"\t\t   ♨  Receita {receitas_escolhida[0]}  ♨")
    print("==========================================================")
    print(f"Ingredientes:\n\n⚬ {receitas_escolhida[2]}\n")
    print(f"Modo de preparo:\n\n☛  {receitas_escolhida_passos[3]}")
    print("==========================================================")


def visualizar_receita():
    receitas = obter_receitas()
    receita_selecionada = selecionar_receita_view(receitas)
    exibir_receita(receita_selecionada)
    input("Pressione Enter para voltar ao menu principal: ")

def edit_nome_receita(receita_selecionada):
    os.system('cls')
    novo_nome = input("Digite o novo nome para a receita: ")

    with open("Repositorio_de_receitas.txt", "r+", encoding="utf8") as arquivo:
        linhas_arquivo = arquivo.readlines()
        arquivo.seek(0)
        for linha in linhas_arquivo:
            if receita_selecionada in linha:
                nova_linha = linha.replace(receita_selecionada, novo_nome)
                arquivo.write(nova_linha)
            else:
                arquivo.write(linha)
        arquivo.truncate()
    
    print("Nome da receita atualizado com sucesso!")

def edit_ingredientes_receita():
    'teste'

def edit_preparo_receita():
    'teste'

def atualizar():
    receitas = obter_receitas()
    receita_selecionada = selecionar_receita_edit(receitas)
    exibir_receita(receita_selecionada)
    
    opcao_escolhida_edit = int(input("Digite:\n\n(1) Para editar o nome da receita.\n(2) Para editar os ingredientes.\n(3) Para editar o modo de preparo.\n\n"))

    if opcao_escolhida_edit == 1:
        edit_nome_receita(receita_selecionada)


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
    

#==================================  MENU PRINCIPAL  ==================================================#
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
    acao = str(input("\nDigite qual ação deseja realizar: "))

    menu_interativo(acao) # roda/printa a função escolhida

    if acao == '0':
        break
    else: 
        continue
    
#======================================================================================================#
