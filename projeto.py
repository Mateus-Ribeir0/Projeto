import os
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

    nova_receita = '\n' + ' - '.join(formatador) + '-False'
    file.write(nova_receita)

    file.close()

def visualizar():


    return 'teste2'

def atualizar():


    return 'teste3'

def excluir():


    return 'teste4'

def filtragem():


    return 'teste5'

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