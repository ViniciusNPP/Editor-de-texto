import time
import os
import re
import Aparencia.ap_editores as ap

def EditarTexto(texto):
    if len(texto) == 0:
        os.system("cls")
        return None
    
    while True:
        opcao = ap.AparenciaEditorTexto()
        
        if opcao == "1" or opcao == "2":
            print("Texto a ser procurado")
            print("Exemplo: ' ==> * ', procura por todos '*' digitados no texto")
            proc = input("==> ")
            
            if opcao == "1":
                print("O que irá substituir o texto digitado acima?")
                subst = input("==> ")
                
                return re.sub(proc, subst, texto)
            
            elif opcao == "2":
                return re.sub(proc, "", texto)
        
        elif opcao == "/":
            os.system("cls")
            break
        
        elif opcao == "0":
            exit()
        
        else:
            time.sleep(1)
            os.system("cls")