import os
import time
import pyperclip as pc
import Aparencia.ap_menu as menu
import Script.Editor_texto as Et

while True:
    opcao = menu.MenuAparencia()
    match opcao:
        case "1":
            os.system("cls")
            while True:
                print("Insira o texto a ser editado")
                pc.copy(Et.EditarTexto(texto = input("==> ")))
                
                if pc.paste() != "None":
                    os.system("cls")
                    print("===============================================")
                    print(pc.paste())
                    print("===============================================")
                    print("(Texto copiado para a sua área de transferência (Ctrl + C))")

                    opcao = menu.PosExecucao()
                    if opcao == "1":
                        os.system("cls")
                        continue
                break
                
            if opcao == "0":
                break
            elif opcao == "/":
                os.system("cls")
            
        case "0":
            break
        case "":
            time.sleep(1)
            os.system("cls")