#========================================
#MÓDULOS DE PROCESSAMENTO (def)
#========================================
def calcular_bonus(salario)
    """calcular o bonus padrao de 15%da Arketech"""
    return salario * 0.15
#========================================
#INTERFACE DO SISTEMA
#========================================
print("========================================")
print("    RH ARKETECH - BONUS INICIAL   ")
print("========================================")

while True:
    print("\n---NOVO REGISTRO---")

    #O .STRIP() REMOVE ESPAÇOS EM BRANCOS DIGITADOS SEM QUERER
    nome = input("Nome completo (ou digite "0" para sair):").strip()

    if nome == "0":
        print("\n Encerramos o painel de bonus.bom trabalho!")
        break
    #blindagem 1: impede que o nome fique em branco se o usuario se apertar "enter"
    if not nome:
        print(" ERRO: O campo de nome não pode ficar vazio. ")
        continue
    cargo = input("Cargo contratado: ").strip()
#