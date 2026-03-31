import os
import time
import pyperclip as pc
import Aparencia.ap_menu as menu
import Script.Editor_texto as Et
import Auxiliar.auxilio as aux
import Script.Operacoes_com_documento.Pegar_texto as PegarTexto

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
            
        case "2": #Editor de documento
            os.system("cls")
            #Lista os arquivos .txt e .pdf do diretório atual, ignorando o requirements.txt
            conteudo = list(filter(lambda x: x.endswith((".txt", ".pdf")) if x != "requirements.txt" else False, os.listdir()))
            
            if len(conteudo) == 0:
                print("Nenhum arquivo .txt ou .pdf encontrado no diretório atual.")
                time.sleep(2)
                os.system("cls")
                continue
            elif len(conteudo) >= 1:
                print("Selecione um dos arquivos abaixo para editar:")
                for i, arquivo in enumerate(conteudo):
                    print(f"{i + 1}- {arquivo}")
                
                #Pega o index do arquivo que o usuário escolher com verificador de opções válidas
                if len(conteudo) > 1:
                    arquivo = int(aux.OpcoesValidas(input("==> "), [str(i + 1) for i in range(len(conteudo))])) - 1
                
                texto = conteudo[arquivo if len(conteudo) > 1 else 0].split(".")[-1]
                match texto:
                    case "txt": texto = PegarTexto.LerTxt(conteudo[arquivo if len(conteudo) > 1 else 0])
                    case "pdf": texto = PegarTexto.LerPdf(conteudo[arquivo if len(conteudo) > 1 else 0])                       
                    case _:
                        print("Tipo de arquivo não suportado.")
                        time.sleep(2)
                        os.system("cls")
                        continue
            
                print(texto)
                
        case "0": #Sair do programa
            break
        case "": #Caso digite alguma coisa opção que não existe
            time.sleep(1)
            os.system("cls")