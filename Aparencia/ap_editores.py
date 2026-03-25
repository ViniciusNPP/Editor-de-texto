import Auxiliar.auxilio as aux

def AparenciaEditorTexto():
    print("===============================================")
    print("==============EDIÇÃO DE TEXTO==============")
    print("===============================================")

    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Substituir texto")
    print("2- Excluir texto")
    print("/- Voltar ao menu anterior")
    print("0- Sair")
    
    return aux.OpcoesValidas(input("==> "), ["1", "2", "/", "0"])