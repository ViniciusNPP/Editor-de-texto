import os

def MenuAparencia():
    print("===============================================")
    print("==============EDIÇÃO DE DOCUMENTO==============")
    print("===============================================")

    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Editar texto")
    print("0- Sair")
    resposta = input("==> ")

    match resposta:
        case "1":
            return resposta
        case "0":
            print("Saindo do programa...")
            return resposta
        case _:
            print("Opção inválida")
            return ""

def PosExecucao(texto):
    os.system("cls")
    print("===============================================")
    print(texto)
    print("===============================================")
    print("(Texto copiado para a sua área de transferência (Ctrl + C))")
    
    print("1- Continuar          0- Sair          /- Voltar ao menu anterior")
    return input("==> ")