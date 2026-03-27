import os
import Auxiliar.auxilio as aux
import Aparencia.ap_menu as menu

def AparenciaSubsituicao():
    os.system("cls")
    print("===============================================")
    print("================SUBSTITUIR TEXTO===============")
    print("===============================================")
    
    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Apenas 1 texto")
    print("2- Mais de 1 texto")
    print("3- Usar regex")
    print("/- Voltar ao menu anterior")
    print("0- Sair")
    
    return aux.OpcoesValidas(input("==> "), ["1", "2", "3", "/", "0"])

def AparenciaSubNormal():
    os.system("cls")
    print("Texto a ser procurado")
    print("Exemplo: '==> * '")
    print("procura por todos '*' digitados no texto")
    proc = input("==> ")
    
    os.system("cls")
    print("Palavra procurada: ", proc)
    print("===============================================")
    print("O que irá substituir o texto digitado acima?")
    subst = input("==> ")
    
    return proc, subst
    
def AparenciaSubSequencia():
    os.system("cls")
    print("Texto a ser procurado")
    print("Exemplo: '==> *, 9, ,'")
    print("O programa irá procurar por todos os *, 9 e , digitados no texto")
    print("IMPORTANTE: É PRECISO DAR ESPAÇO DEPOIS DÁ VÍRGULA, SENÃO O PROGRAMA NÃO VAI ENCONTRAR")
    print("ISSO É SEPARADOR:', ' ISSO NÃO É SEPARADOR:','")
    proc = input("==> ")
    
    os.system("cls")
    print("Palavras procuradas: ", proc)
    print("===============================================")
    print("O que irá substituir o texto digitado acima?")
    print("Se deseja substituir toda a sequência por apenas uma coisa, escreva normalmente")
    print("Senão utilize vírgula, como foi feito anteriormente, para separar as palavras")
    print("Exemplo: '==> ',', 10, |'")
    print("IMPORTANTE:")
    print("1. É PRECISO DAR ESPAÇO DEPOIS DÁ VÍRGULA, SENÃO O PROGRAMA NÃO VAI ENCONTRAR")
    print("2. SE A QUANTIDADE DE PALAVRAS PARA SUBSTITUIR FOR MENOR QUE AS PROCURADAS, AS ÚLTIMAS PALAVRAS PROCURADAS SERÃO SUBSTITUIDAS PELAS AS ÚLTIMAS PALAVRAS PARA SUBSTITUIR")
    subst = input("==> ")
    
    return proc, subst

def AparenciaSubRegex():
    os.system("cls")
    print("Texto a ser procurado")
    print("Exemplo: '==> \d+ , \s*'")
    print("procura por todos números digitados no texto e espaços em branco")
    print("IMPORTANTE: PARA ESCREVER MAIS DE UM REGEX DE BUSCA É PRECISO USAR A VIRGULA DESSA MANEIRA: ' , ' (ESPAÇO VIRGULA ESPAÇO)")
    print("Escreva '/3' para mostrar o guia de comandos regex")
    proc = input("==> ")
    
    if proc == "'/3'":
        menu.HelpRegex()
        proc = input("==> ")
    
    os.system("cls")
    print("Regex a ser usado: ", proc)
    print("===============================================")
    print("O que irá substituir o texto digitado acima?")
    print("Escreva '/3' para mostrar o guia de comandos regex")
    subst = input("==> ")
    
    if subst == "'/3'":
        menu.HelpRegex()
        subst = input("==> ")
    
    return proc, subst