def AparenciaEditorTexto():
    print("===============================================")
    print("==============EDIÇÃO DE TEXTO==============")
    print("===============================================")

    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Substituir texto")
    print("2- Excluir texto")
    print("/- Voltar ao menu anterior")
    print("0- Sair")
    
    answer = input("==> ")
    
    match answer:
        case "1":
            return "1"
        case "2":
            return "2"
        case "0":
            print("Saindo do programa...")
            return "0"
        case "/":
            print("Voltando ao menu anterior...")
            return "/"
        case _:
            print("Opção inválida")
            return ""