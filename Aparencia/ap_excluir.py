import os
import Auxiliar.auxilio as aux
import Aparencia.ap_menu as menu

def AparenciaExclusao():
    os.system("cls")
    print("===============================================")
    print("=================EXCLUIR TEXTO=================")
    print("===============================================")
    
    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Apenas 1 texto")
    print("2- Mais de 1 texto")
    print("3- Usar regex")
    print("/- Voltar ao menu anterior")
    print("0- Sair")
    
    return aux.OpcoesValidas(input("==> "), ["1", "2", "3", "/", "0"])

def ConfirmacaoExclusao(proc):
    os.system("cls")
    print("Tem certeza que deseja excluir '",proc,"' do texto?")
    print("S- sim")
    print("N- não")
    if input("==> ").lower() == "s":
        return proc
    return ""

def AparenciaExclusaoNormal():
    os.system("cls")
    print("Texto a ser excluido")
    print("Exemplo: '==> Legal'")
    print("Exclui todos os 'Legal' presentes no texto")
    proc = input("==> ")
    
    os.system("cls")
    return ConfirmacaoExclusao(proc)

def AparenciaExclusaoSequencia():
    os.system("cls")
    print("Texto a ser excluido")
    print("Exemplo: '==> Legal, errado, 1.'")
    print("Exclui todos os 'Legal', 'errado' e '1' presentes no texto")
    print("IMPORTANTE: É PRECISO DAR ESPAÇO DEPOIS DÁ VÍRGULA, SENÃO O PROGRAMA NÃO VAI ENCONTRAR")
    proc = input("==> ")
    
    os.system("cls")
    return ConfirmacaoExclusao(proc)

def AparenciaExclusaoRegex():
    os.system("cls")
    print("Texto a ser excluido")
    print("Exemplo: '==> \d+'")
    print("Exclui todos os números presentes no texto")
    print("Escreva '/3' para mostrar o guia de comandos regex")
    proc = input("==> ")
    
    if proc == "'/3'":
        menu.HelpRegex()
        proc = input("==> ")
    return ConfirmacaoExclusao(proc)