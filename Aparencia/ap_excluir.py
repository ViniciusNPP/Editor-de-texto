import os
import Auxiliar.auxilio as aux

def AparenciaExclusao():
    os.system("cls")
    print("===============================================")
    print("=================EXCLUIR TEXTO=================")
    print("===============================================")
    
    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Apenas 1 texto")
    print("2- Mais de 1 texto")
    print("/- Voltar ao menu anterior")
    print("0- Sair")
    
    return aux.OpcoesValidas(input("==> "), ["1", "2", "/", "0"])

def AparenciaExclusaoNormal():
    os.system("cls")
    print("Texto a ser excluido")
    print("Exemplo: '==> Legal'")
    print("Exclui todos os 'Legal' presentes no texto")
    proc = input("==> ")
    
    os.system("cls")
    print("Tem certeza que deseja excluir '",proc,"' do texto?")
    print("S- sim")
    print("N- não")
    if input("==> ").lower() == "s":
        return proc
    return ""

def AparenciaExclusaoSequencia():
    os.system("cls")