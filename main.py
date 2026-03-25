import os
import time
import pyperclip as pc
import Aparencia.ap_menu as menu
import Script.Editor_texto as Et

while True:
    os.system("cls")
    opcao = menu.MenuAparencia()
    match opcao:
        case "1": #Editor de texto
            os.system("cls")
            while True:
                print("Insira o texto a ser editado")
                pc.copy(Et.EditarTexto(texto = input("==> "))) #Copia o texto para o Ctrl + C do usuário
                
                if pc.paste() != "None": #Verifica se o texto é vazio
                    opcao = menu.PosExecucao(pc.paste())
                    
                    if opcao == "1":
                        os.system("cls")
                        continue
                break
                
            if opcao == "0": #Sair do programa
                break
            elif opcao == "/": #Volta ao menu anterior
                os.system("cls")
            
        case "0": #Sair do programa
            break
        case "": #Caso digite alguma coisa opção que não existe
            time.sleep(1)
            os.system("cls")