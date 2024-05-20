import os
import time
import random

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
    elif acao == '6':
        return MenuFavoritos()
    elif acao == '7':
        return func_randomicas()
    elif acao== '8':
        return visualizar_menores()
    elif acao == '0':
        os.system('cls')
        return print('''
██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║██╔══██╗
██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║███████║
██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║
██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

███████╗███╗░░██╗░█████╗░███████╗██████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██╔██╗██║██║░░╚═╝█████╗░░██████╔╝██████╔╝███████║██║░░██║██║░░██║
██╔══╝░░██║╚████║██║░░██╗██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██║░░██║
███████╗██║░╚███║╚█████╔╝███████╗██║░░██║██║░░██║██║░░██║██████╔╝╚█████╔╝
╚══════╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░''')
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
    try:
        nome = str(input("Nome do prato: "))

        if len(nome)<3:
            tratarErroTamanho()
        else:

            lista_de_cadastro.append(nome)

            print("==========================")
            pais = str(input("País de origem: ")).capitalize()

            if len(pais)<3:
                tratarErroTamanho()
            else:

                lista_de_cadastro.append(pais)

                print("==========================")
                receita_de_ingredientes = []
                quant_de_ingredientes = int(input("Quantidade de ingredientes: "))

                if quant_de_ingredientes==0:
                    tratarErroGeral()
                else:
                    for posicao in range (quant_de_ingredientes):
                        ingrediente = str(input(f"Digite o {posicao+1}° Ingrediente: ").strip().capitalize())
                        receita_de_ingredientes.append(ingrediente)
                    juncao_ingredientes = "|".join(receita_de_ingredientes)
                    lista_de_cadastro.append(juncao_ingredientes)

                    print("==========================")
                    
                    passos = []
                    quant_de_passos = int(input("Quantidade de passos: "))
                    
                    if quant_de_passos==0:
                        tratarErroGeral()
                    else:    
                        for posicao in range (quant_de_passos):
                            modo = str(input(f"Digite o {posicao+1}° passo: ").strip().capitalize())
                            passos.append(modo)
                            juncao_passos = "|".join(passos)
                            lista_de_cadastro.append(juncao_passos)
                            print("==========================")
                            

                            nova_receita = '\n' + ' - '.join(lista_de_cadastro) + ' - False'+ f" - {quant_de_ingredientes}"
                            file.write(nova_receita)

                            file.close()
    except ValueError:
         print("==========================")
         tratarErroGeral_sem_o_texto()
         input("\n\nDigite de forma numerica!, Aperte qualquer tecla para voltar")
        
def obter_receitas():
    os.system('cls')
    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        linhas_arquivo = arquivo.readlines()
    
    receitas = []
    for linha in linhas_arquivo:
        partes = linha.split(' - ')
        receitas.append(partes[0])
    
    return receitas

def selecionar_receitass_view(receitas):
    os.system('cls')

    titulo='''
█░█ █ █▀ █░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█
▀▄▀ █ ▄█ █▄█ █▀█ █▄▄ █ █▄ █▀█ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▀▄ ██▄ █▄▄ ██▄ █ ░█░ █▀█\n'''
    print(titulo)
    try:
        for i, receita in enumerate(receitas, 1):
            print(f"{i:^2} - {receita}")

        print("==========================================================")
        numero_str = input("Digite o número da receita que você quer ver: ")
        
        if not numero_str.strip():
            os.system('cls')
            print("Código deu erro. Nenhum número foi fornecido.")
            time.sleep(2)
            os.system('cls')
            return selecionar_receitass_view(receitas)
        
        numero = int(numero_str)
        if numero==0:
            print("==========================")
            tratarErroGeral_sem_o_texto()
            input("\n\nDigite um numero que esteja dentro do intervalo demonstado! Aperte qualquer tecla para voltar:")
        
            return menu_interativo(acao)
        else:
        
       
            return receitas[numero - 1]
        
            

    except IndexError:
        print("==========================")
        tratarErroGeral_sem_o_texto()
        input("\n\nDigite um numero que esteja dentro do intervalo demonstado! Aperte qualquer tecla para voltar:")
        
        return menu_interativo(acao)
    except TypeError:
        input("pressione enter para voltar ao menu")
        return menu_interativo(acao)


def selecionar_receitass_edit(receitas):
    titulo='''
▄▀█ ▀█▀ █░█ ▄▀█ █░░ █ ▀█ ▄▀█ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█
█▀█ ░█░ █▄█ █▀█ █▄▄ █ █▄ █▀█ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▀▄ ██▄ █▄▄ ██▄ █ ░█░ █▀█ \n'''
    print(titulo)
    try:
        for i, receita in enumerate(receitas, 1):
            print(f"{i:^2} - {receita}")

        print("==========================================================")
        numero = int(input("Digite o número da receita que você quer editar: "))
        if numero==0:
                print("==========================")
                tratarErroGeral_sem_o_texto()
                input("\n\nDigite um numero que esteja dentro do intervalo demonstado! Aperte qualquer tecla para voltar:")
            
                return menu_interativo(acao)
        else:
            return receitas[numero - 1]
    except IndexError:
        print("==========================")
        tratarErroGeral_sem_o_texto()
        input("\n\nDigite um numero que esteja dentro do intervalo demonstado! Aperte qualquer tecla para voltar:")
        
        return menu_interativo(acao)   

def exibir_receitass(receita):
    os.system('cls')
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
                        nomes_juntos_passos = '\n☛  '.join(nomes_separados)
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
    receita_selecionada = selecionar_receitass_view(receitas)
    exibir_receitass(receita_selecionada)
    input("Pressione Enter para voltar ao menu principal: ")

def edit_nome_receita(receita_selecionada):
    os.system('cls')
    novo_nome = input("Digite o novo nome para a receita: ")

    if not novo_nome.strip():
        os.system('cls')
        print("Nome inválido, digite um novo.")
        time.sleep(2)
        return edit_nome_receita(receita_selecionada)
    

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
    print("===========================================")
    input("Pressione Enter para voltar ao menu principal")

def edit_ingredientes_receita(receita_selecionada):
    os.system('cls')
    try:
        ingredientes = []
        nmrdeingredientes = int(input("Digite a nova quantidade de ingredientes: "))
        print("===============================================")

        for numeracao in range(nmrdeingredientes):
            while True:
                novos_ingredientes = input(f"Diga o {numeracao+1} ingrediente: ").strip()
                if all(caractere.isalpha() or caractere.isspace() for caractere in novos_ingredientes):
                    novos_ingredientes1 = novos_ingredientes.capitalize()
                    ingredientes.append(novos_ingredientes1)
                    break
                else:
                    print("Ingrediente inválido, digite apenas letras. Tente novamente.")

        if not ingredientes[-1].strip():
            os.system('cls')
            print("Ingrediente inválido, digite novamente")
            time.sleep(2)
            return edit_ingredientes_receita(receita_selecionada)

        leituraarquivo = '|'.join(ingredientes)

        with open("Repositorio_de_receitas.txt", "r+", encoding="utf8") as nmringredientes:
            partedoarquivo = nmringredientes.readlines()
            nmringredientes.seek(0)

            for linha in partedoarquivo:
                if receita_selecionada in linha:
                    partes = linha.strip().split(' - ', 4)
                    if len(partes) >= 4:
                        linha_nova = partes[0] + ' - ' + partes[1] + ' - ' + leituraarquivo + ' - ' + partes[3] + ' - ' + 'False\n'
                        nmringredientes.write(linha_nova)
                    else:
                        nmringredientes.write(linha)
                else:
                    nmringredientes.write(linha)
            nmringredientes.truncate()

        print("\nIngredientes Alterados com Sucesso!\n\n")
        print("======================================================")
        input("Pressione Enter Para Voltar ao menu principal")
    except ValueError:
        tratarErroGeral()    

def edit_preparo_receita(receita_selecionada):
    os.system('cls')
    try:
        lista_preparo = []
        qntd_de_preparo = int(input("Digite a quantidade de novos passos: "))
        print("====================================")
        
        for posicao in range(qntd_de_preparo):
            while True:
                novo_modo_preparo = input(f"Digite o {posicao+1}° passo: ").strip().capitalize()
                if all(caractere.isalpha() or caractere.isspace() for caractere in novo_modo_preparo):
                    lista_preparo.append(novo_modo_preparo)
                    break
                else:
                    print("Passo inválido, digite apenas letras. Tente novamente.")

        if not lista_preparo[-1].strip():
            os.system('cls')
            print("Passo inválido, digite novamente.")
            time.sleep(2)
            return edit_preparo_receita(receita_selecionada)

        novo_preparo = '|'.join(lista_preparo)

        with open("Repositorio_de_receitas.txt", "r+", encoding="utf8") as arquivo:
            linhas_arquivo = arquivo.readlines()
            arquivo.seek(0)

            for linha in linhas_arquivo:
                if receita_selecionada in linha:
                    partes = linha.strip().split(' - ', 4)
                    if len(partes) >= 4:
                        nova_linha = partes[0] + ' - ' + partes[1] + ' - ' + partes[2] + ' - ' + novo_preparo + ' - ' + 'False\n'
                        arquivo.write(nova_linha)
                    else:
                        arquivo.write(linha)
                else:
                    arquivo.write(linha)
            
            arquivo.truncate()

        print("\nModo de preparo das receitas atualizado com sucesso!\n\n")
        print("======================================================")
        input("Pressione Enter Para Voltar ao menu principal")
    except ValueError:
        tratarErroGeral()
        
def atualizar():
    try: 
        receitas = obter_receitas()
        receita_selecionada = selecionar_receitass_edit(receitas)
        exibir_receitass(receita_selecionada)
    
        opcao_escolhida_edit = int(input("Digite:\n\n(1) Para editar o nome da receita.\n(2) Para editar os ingredientes.\n(3) Para editar o modo de preparo.\n\n"))

        if opcao_escolhida_edit == 1:
            edit_nome_receita(receita_selecionada)
        elif opcao_escolhida_edit == 2:
            edit_ingredientes_receita(receita_selecionada)
        elif opcao_escolhida_edit == 3:
            edit_preparo_receita(receita_selecionada)
        else:
            print("Opção invalida.")
    except ValueError:
        tratarErroGeral()

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

def MenuFavoritos():
    os.system('cls')
    titulo = '''

█▀▄▀█ █▀▀ █▄ █ █ █   █▀▄ █▀▀   █▀▀ ▄▀█ █ █ █▀█ █▀█ █ ▀█▀ █▀█ █▀
█ ▀ █ ██▄ █ ▀█ █▄█   █▄▀ ██▄   █▀  █▀█ ▀▄▀ █▄█ █▀▄ █  █  █▄█ ▄█\n\n'''

    print(titulo)
    print("1 - Lista de favoritos")
    print("2 - Adicionar receita a favoritos")
    print("3 - Excluir receita de favoritos")
    print("0 - Voltar ao menu principal")
    escolha = str(input("\nDigite qual ação deseja realizar: "))

    if escolha == '1':
        return ListaFavoritos()
    elif escolha == '2':
        return AdicionarFavoritos()
    elif escolha == '3':
        return ExcluirFavoritos()
    elif escolha == '0':
        return 
    else:
        print("\nOpção Inválida! Digite outra opção.")
        time.sleep(2)
        return
    
def ExcluirFavoritos():
    os.system('cls')
    titulo = '''
█▀▀ ▀▄▀ █▀▀ █   █ █ █ █▀█   █▀▄ █▀▀   █▀▀ ▄▀█ █ █ █▀█ █▀█ █ ▀█▀ █▀█ █▀
██▄ █ █ █▄▄ █▄▄ █▄█ █ █▀▄   █▄▀ ██▄   █▀  █▀█ ▀▄▀ █▄█ █▀▄ █  █  █▄█ ▄█\n\n'''
    print(titulo)

    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        linhas_arquivo = arquivo.readlines()
    
    favoritos = []
    for receita in linhas_arquivo:
        linha = receita.strip().split(' - ')
        if len(linha) >= 5 and linha[4].strip() == 'True':
            favoritos.append(linha)

    if not favoritos:
        print("Não há receitas marcadas como favoritas.")
        input("\nPressione Enter para voltar ao menu principal: ")
        return
    
    for i, receita in enumerate(favoritos, 1):
        print(f"{i} - {receita[0]}")

    print("==========================================================")

    escolhido = input("Digite o número da receita que deseja excluir dos favoritos: ")
    
    if not escolhido.strip() or not escolhido.isdigit() or int(escolhido) < 1 or int(escolhido) > len(favoritos):
        print("Escolha inválida.")
        input("\nPressione Enter para voltar ao menu principal: ")
        return
    
    numero = int(escolhido)

    linha_escolhida = favoritos[numero - 1]
    linha_escolhida[-1] = 'False'

    with open("Repositorio_de_receitas.txt", "w", encoding="utf8") as arquivo:
        for linha in linhas_arquivo:
            if linha.strip().split(' - ')[0] == linha_escolhida[0]:
                arquivo.write(' - '.join(linha_escolhida) + '\n')
            else:
                arquivo.write(linha)

    input("\nPressione Enter para voltar ao menu principal: ")

def AdicionarFavoritos():
    os.system('cls')
    titulo =  '''
▄▀█ █▀▄ █ █▀▀ █ █▀█ █▄ █ ▄▀█ █▀█   ▄▀█ █▀█ █▀   █▀▀ ▄▀█ █ █ █▀█ █▀█ █ ▀█▀ █▀█ █▀
█▀█ █▄▀ █ █▄▄ █ █▄█ █ ▀█ █▀█ █▀▄   █▀█ █▄█ ▄█   █▀  █▀█ ▀▄▀ █▄█ █▀▄ █  █  █▄█ ▄█\n\n'''
    print(titulo)

    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        linhas_arquivo = arquivo.readlines()
    
    receitas = []

    for linha in linhas_arquivo:
        partes = linha.split(' - ')
        receitas.append(partes[0])

    listareceitas = obter_receitas()
    
    for i, receita in enumerate(receitas, 1):
        print(f"{i:^2} - {receita}")

    print("==========================================================")
    escolhido = str(input("Digite a posição da receita que deseja adicionar aos favoritos: "))
    
    if not escolhido.strip():
        os.system('cls')
        print("Código deu erro. Nenhum número foi fornecido.")
        time.sleep(2)
        os.system('cls')
        return selecionar_receitass_view(receitas)
    
    numero = int(escolhido)

    linha_escolhida = linhas_arquivo[numero - 1].strip()
    partes = linha_escolhida.split(' - ')
    partes[-1] = 'True'
    linhas_arquivo[numero - 1] = ' - '.join(partes) + '\n'

    with open("Repositorio_de_receitas.txt", "w", encoding="utf8") as arquivo:
        arquivo.writelines(linhas_arquivo)

    return receitas[numero - 1]

def tratarErroGeral():
    os.system('cls')
    print('''
███████╗██████╗░██████╗░░█████╗░  ██████╗░███████╗████████╗███████╗░█████╗░████████╗░█████╗░██████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║  ██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░███████║██║░░██║██║░░██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║  ██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██╔══██║██║░░██║██║░░██║
███████╗██║░░██║██║░░██║╚█████╔╝  ██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝░░░██║░░░██║░░██║██████╔╝╚█████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░\n\n''')
    return str(input("Opção invalida. Aperte qualquer tecla para voltar ao menu principal: "))

def tratarErroTamanho():
    os.system('cls')
    print('''
███████╗██████╗░██████╗░░█████╗░  ██████╗░███████╗████████╗███████╗░█████╗░████████╗░█████╗░██████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║  ██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░███████║██║░░██║██║░░██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║  ██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██╔══██║██║░░██║██║░░██║
███████╗██║░░██║██║░░██║╚█████╔╝  ██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝░░░██║░░░██║░░██║██████╔╝╚█████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░\n\n''')
    return str(input("Não é permitido o cadastro de nada com menos de 3 caracteres: "))

def tratarErroGeral_sem_o_texto():
    os.system('cls')
    print('''
███████╗██████╗░██████╗░░█████╗░  ██████╗░███████╗████████╗███████╗░█████╗░████████╗░█████╗░██████╗░░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║  ██║░░██║█████╗░░░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░███████║██║░░██║██║░░██║
██╔══╝░░██╔══██╗██╔══██╗██║░░██║  ██║░░██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██╔══██║██║░░██║██║░░██║
███████╗██║░░██║██║░░██║╚█████╔╝  ██████╔╝███████╗░░░██║░░░███████╗╚█████╔╝░░░██║░░░██║░░██║██████╔╝╚█████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░\n\n''')

def ListaFavoritos():
    
    os.system('cls')

    file = open('Repositorio_de_receitas.txt', 'r', encoding='utf8')
    lista_de_receitas = file.readlines()
    file.close()

    titulo = '''
█   █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀▀ ▄▀█ █ █ █▀█ █▀█ █ ▀█▀ █▀█ █▀
█▄▄ █ ▄█  █  █▀█   █▄▀ ██▄   █▀  █▀█ ▀▄▀ █▄█ █▀▄ █  █  █▄█ ▄█\n\n'''

    print(titulo)
    receitas_e_favoritos = [receita.strip().split(' - ') for receita in lista_de_receitas]

    opcao = input("Digite (F) para visualizar as receitas favoritas e (N) para as que não são favoritas: ").upper()

    if opcao == 'F':
        favorito_filtrado = True
    elif opcao == 'N':
        favorito_filtrado = False
    else:
        tratarErroGeral()
    
        

    receitas_filtradas = [receita for receita in receitas_e_favoritos if (receita[4] == 'True') == favorito_filtrado]
    os.system('cls')
    print(titulo)
    print("==========================================================")
    if favorito_filtrado:
        print("\t\tReceitas Favoritas")
    else:
        os.system('cls')
        print(titulo)
        print("\t\tReceitas Não Favoritas")
    print("==========================================================")


    nomes_das_receitas = []
    j = 1
    for receita in receitas_filtradas:
        nome = receita[0]
        nomes_das_receitas.append(nome)
        print(f"{j} - {nome}")
        j += 1

    print("==========================================================")
    if j == 1:
        print("Não há receitas disponíveis.")
    else:
        indice_receita_escolhida = int(input("Receita: "))
        os.system('cls')
        if indice_receita_escolhida > j:
            return str(input("Opção invalida. Aperte qualquer tecla para voltar ao menu principal: "))
        else:
            receita_escolhida = receitas_filtradas[indice_receita_escolhida - 1]

            print(f"\t ♨  Receita {receita_escolhida[0]}  ♨")
            print("==========================================================")
            print(f"Ingredientes:\n\n⚬ {'\n⚬ '.join(receita_escolhida[2].split('|'))}\n")
            print(f"Modo de preparo:\n\n☛  {'\n☛  '.join(receita_escolhida[3].split('|'))}")
            print("==========================================================")

    voltar = str(input("Aperte qualquer tecla para voltar ao menu principal: "))

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

    try:
        pais_filtrado = int(input("Escolha o país o qual deseja visualizar as receitas: "))

        if pais_filtrado == 0:
            return tratarErroGeral()
        else:
            os.system('cls')

            receitas_filtradas = []
            for receita in lista_de_paises:  # Separando as receitas do país escolhido em uma lista
                pais_escolhido = receita.split(' - ')

                if paises[pais_filtrado - 1] == pais_escolhido[1]:
                    receitas_filtradas.append(receita)

            print(f"\t\tReceitas do(a) {paises[pais_filtrado - 1]}  ")
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

        if indice_receita_escolhida == 0:
            return tratarErroGeral()
        else:
            receita_escolhida = []
            receita_escolhida_passos = []
            for receita in receitas_filtradas:  # adicionando a receita escolhida em uma lista
                if nomes_das_receitas[indice_receita_escolhida - 1] in receita:
                    receita_separada = receita.split(' - ')

                    for k in receita_separada:  # formatando os nomes para uma melhor leitura
                        if '|' in k and len(k) >= 2:
                            nome_separado = k.split('|')
                            nome_junto = '\n⚬ '.join(nome_separado)
                            nome_junto_passos = '\n☛  '.join(nome_separado)
                            receita_escolhida.append(nome_junto)
                            receita_escolhida_passos.append(nome_junto_passos)
                        else:
                            receita_escolhida.append(k)
                            receita_escolhida_passos.append(k)

            os.system('cls')

            print(f"\t\t ♨  Receita {receita_escolhida[0]}  ♨")
            print("==========================================================")
            print(f"Ingredientes:\n\n⚬ {receita_escolhida[2]}\n")
            print(f"Modo de preparo:\n\n☛  {receita_escolhida_passos[3]}")
            print("==========================================================")
            voltar = str(input("Aperte qualquer tecla para voltar ao menu principal: "))

    except ValueError:
        tratarErroGeral()
    except IndexError:
        tratarErroGeral()
        
def func_randomicas():
    os.system('cls')  
    with open('Repositorio_de_receitas.txt', 'r', encoding='utf8') as arquivoR:
        receitas = arquivoR.readlines()

    titulo2= '''
▒█▀▀█ █▀▀ █▀▀ █▀▀ ░▀░ ▀▀█▀▀ █▀▀█ 　 █▀▀█ █░ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ ░▀░ █▀▀█ 
▒█▄▄▀ █▀▀ █░░ █▀▀ ▀█▀ ░░█░░ █▄▄█ 　 █▄▄█ █░ █▀▀ █▄▄█ ░░█░░ █░░█ █▄▄▀ ▀█▀ █▄▄█ 
▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀   ▀   ▀  ▀ 　 █  █ ▀▀ ▀▀▀ ▀  ▀   ▀   ▀▀▀▀ ▀ ▀▀ ▀▀▀ ▀  ▀'''
    print(titulo2)
    receita_aleatoria = random.choice(receitas).strip().split(' - ')

    print("\n")
    print("Nome:", receita_aleatoria[0])
    print("====================================")
    print("País:", receita_aleatoria[1])
    print("====================================")
    print("Ingredientes:")
    for ingrediente in receita_aleatoria[2].strip().split('|'):
        print("-", ingrediente)
    print("====================================")
    print("Modo de Preparo:")
    for passo in receita_aleatoria[3].strip().split('|'):
        print("-", passo)
    print("====================================")          
    input("Pressione enter para voltar ao menu principal: ")

def func_extra():
    os.system('cls')
    with open('Repositorio_de_receitas.txt', 'r', encoding='utf8') as arquivoR:
        lista_ingredientes = []
        lista_de_nomes = []
        lista_da_receitamenor = []
        lista_de_nomes_exibicao = []
        
        receitas = arquivoR.readlines()
        for receita in receitas:
            ingredientes = receita.split(" - ")
            ingredientess = ingredientes[5].strip()
            lista_ingredientes.append(ingredientess)
            lista_de_nomes.append(ingredientes[0].strip())
        
        min_ingredientes = min(lista_ingredientes) 
        for i in range(len(lista_ingredientes)):
            if lista_ingredientes[i] == min_ingredientes:
                if lista_de_nomes[i] in receitas[i]:
                    lista_da_receitamenor.append(receitas[i])
                    lista_de_nomes_exibicao.append(lista_de_nomes[i])
        
        return lista_de_nomes_exibicao

def selecionar_receita_views(lista_de_nomes_exibicao):
    os.system('cls')
    titulo='''
█▀▄▀█ █▀▀ █▄░█ █▀█ █▀█ █▀▀ █▀   █▀█ █▀▀ █▀▀ █▀▀ █ ▀█▀ ▄▀█ █▀
█░▀░█ ██▄ █░▀█ █▄█ █▀▄ ██▄ ▄█   █▀▄ ██▄ █▄▄ ██▄ █ ░█░ █▀█ ▄█\n'''
    print(titulo)
    for i, receita in enumerate(lista_de_nomes_exibicao, 1):
        print(f"{i:^2} - {receita}")

    print("==========================================================")
    numero_str = input("Digite o número da receita que você quer ver: ")
    
    if not numero_str.strip():
        os.system('cls')
        print("Código deu erro. Número inválido.")
        time.sleep(2)
        os.system('cls')
        return selecionar_receita_views(lista_de_nomes_exibicao)
    
    numero = int(numero_str)
    return lista_de_nomes_exibicao[numero - 1]

def exibir_receitasss(receita_nome):
    os.system('cls')
    receitas_escolhida = []
    receitas_escolhida_passos = []

    with open("Repositorio_de_receitas.txt", "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            if receita_nome in linha:
                partes = linha.split(' - ')
                for parte in partes:
                    if '|' in parte and len(parte) >= 2:
                        nomes_separados = parte.split('|')
                        nomes_juntos = '\n⚬ '.join(nomes_separados)
                        nomes_juntos_passos = '\n☛  '.join(nomes_separados)
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

def visualizar_menores():
    receitass = func_extra()
    receita_selecionadass = selecionar_receita_views(receitass)
    exibir_receitasss(receita_selecionadass)
    input("Pressione Enter para voltar ao menu principal: ")


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
    print("6 - Favoritos")
    print("7 - Sugestão de Receita Aleatória")
    print("8 - Menores receitas")
    print("0 - Sair do programa")
    acao = str(input("\nDigite qual ação deseja realizar: "))

    menu_interativo(acao) # roda/printa a função escolhida

    if acao == '0':
        break
    else: 
        continue
    
#======================================================================================================#
