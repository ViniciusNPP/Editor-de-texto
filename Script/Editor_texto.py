import time
import os
import Aparencia.ap_editores as ap
import Aparencia.ap_substituir as ap_sub
import Aparencia.ap_excluir as ap_ex
import Script.Operacoes_de_edicao.Substituicao as sub
import Script.Operacoes_de_edicao.Exclusao as ex

'''
A FAZER
1. SUBSTITUIR TEXTO USANDO COMANDOS REGEX
    1.1. PERMITIR O USUÁRIO ESCREVER O COMANDO REGEX
    1.2. LISTA DOS COMANDOS REGEX PARA O USUÁRIO VER
2. EXCLUIR TEXTO
3. EXCLUIR TEXTO USANDO REGEX
4. FAZER SUBSTITUIÇÃO E EXCLUSÃO DE TEXTO EM ARQUIVO .TXT E .PDF
'''

def EditarTexto(texto):
    if len(texto) == 0:
        os.system("cls")
        return None
    
    while True:
        opcao = ap.AparenciaEditorTexto()
        
        if opcao == "1":
            while True:
                opcao = ap_sub.AparenciaSubsituicao()
                
                if opcao == "1":
                    return sub.SubstituirNormal(texto)
                elif opcao == "2":
                    return sub.SubstituirSequencia(texto)
                break
            if opcao == "0":
                exit()
            
            os.system("cls")
            
        elif opcao == "2":
            while True:
                opcao = ap_ex.AparenciaExclusao()
                
                if opcao == "1":
                    return ex.ExcluirNormal(texto)
                elif opcao == "2":
                    return ex.ExcluirSequencia(texto)
                break
            
            if opcao == "0":
                exit()
            
            os.system("cls")
            
        elif opcao == "/":
            os.system("cls")
            break
        
        elif opcao == "0":
            exit()
        
        else:
            time.sleep(1)
            os.system("cls")