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
            return "1"
        case "0":
            print("Saindo do programa...")
            return "0"
        case _:
            print("Opção inválida")
            return ""

def PosExecucao():
    print("1- Continuar          0- Sair          /- Voltar ao menu anterior")
    return input("==> ")