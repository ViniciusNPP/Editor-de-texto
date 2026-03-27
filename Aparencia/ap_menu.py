import os

def MenuAparencia():
    print("===============================================")
    print("==============EDIÇÃO DE DOCUMENTO==============")
    print("===============================================")

    print("SELECIONE UMA DAS OPÇÕES ABAIXO:")
    print("1- Editar texto")
    print("0- Sair")
    resposta = input("==> ")

    match resposta:
        case "1":
            return resposta
        case "0":
            print("Saindo do programa...")
            return resposta
        case _:
            print("Opção inválida")
            return ""

def PosExecucao(texto):
    os.system("cls")
    print("===============================================")
    print(texto)
    print("===============================================")
    print("(Texto copiado para a sua área de transferência (Ctrl + C))")
    
    print("1- Continuar          0- Sair          /- Voltar ao menu anterior")
    return input("==> ")

def HelpRegex():
    print("\n================ GUIA REGEX ================")
    print("--- SELETORES (O que buscar) ---")
    print(r"\d  - Qualquer número (0-9)")
    print(r"\D  - Qualquer coisa que NÃO seja número")
    print(r"\w  - Letra, número ou underline (_)")
    print(r"\W  - Qualquer símbolo ou espaço (NÃO alfanumérico)")
    print(r"\s  - Espaços em branco, tabs ou quebras de linha")
    print(r"\S  - Qualquer coisa que NÃO seja espaço")
    print(r".   - Qualquer caractere (o 'curinga')")
    
    print("\n--- QUANTIFICADORES (Quantas vezes) ---")
    print(r"+   - O item anterior deve aparecer 1 ou mais vezes")
    print(r"* - O item anterior pode aparecer 0 ou mais vezes")
    print(r"?   - O item anterior é opcional (0 ou 1 vez)")
    print(r"{n} - Exatamente 'n' vezes (ex: \d{3} pega 3 números)")
    
    print("\n--- ÂNCORAS E LÓGICA (Onde e Como) ---")
    print(r"^   - O padrão deve estar no INÍCIO da linha")
    print(r"$   - O padrão deve estar no FIM da linha")
    print(r"|   - Operador 'OU' (ex: gato|cao)")
    print(r"[]  - Lista de caracteres (ex: [abc] busca a, b ou c)")
    print(r"[^] - Negação (ex: [^0-9] busca o que NÃO é número)")
    print(r"\b  - Limite de palavra (evita pegar partes de palavras)")
    print("======================================================\n")
    
    print("\n--- GRUPOS E RETROVISORES (Capturar e Reutilizar) ---")
    print(r"()  - Grupo de Captura: Salva o que foi achado em uma memória.")
    print(r"      Ex: (\d+) salva um grupo de números.")
    print(r"\1  - Chama o 1º grupo salvo para usá-lo na substituição.")
    print(r"      Ex: Substituir (\w+) por [\1] coloca a palavra em colchetes.")
    print(r"\2, \3 - Chama o 2º, 3º grupo (e assim por diante).")
    print("======================================================\n")
    
    print("\n--- COMANDOS DE TRANSFORMAÇÃO ---")
    print(r"\L1  - Transforma o Grupo 1 em minúsculas (lower)")
    print(r"\U1  - Transforma o Grupo 1 em maiúsculas (upper)")
    print(r"\C1  - Capitaliza o Grupo 1 (olá MUNDO -> Olá mundo)")
    print(r"\AU1  - Todas as palavras do Grupo 1 tem iniciais maiúsculas (olá mundo -> Olá Mundo)")