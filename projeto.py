import os
os.system('cls')

def menu_interativo(acao):
    if acao == 'A':
        return adicionar()
    elif acao == 'V':
        return visualizar()
    elif acao == 'R':
        return atualizar()
    elif acao == 'E':
        return excluir()
    elif acao == 'F':
        return filtragem()
    else:
        return 'Ação inválida'
            
def adicionar():


    return 'teste1'

def visualizar():


    return 'teste2'

def atualizar():


    return 'teste3'

def excluir():


    return 'teste4'

def filtragem():


    return 'teste5'

#============ MENU =======================#
print("======{ Menu do Programa }======\n")
print("A - Adicionar receita")
print("V - Visualizar receitas ")
print("R - Atualizar receitas")
print("E - Excluir receita")
print("F - Filtragem por País")
acao = str(input("\nAção: ").upper())
#=========================================#

print(menu_interativo(acao))


        



