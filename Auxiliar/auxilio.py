def OpcoesValidas(resposta, opcoes_validas):
    if resposta in opcoes_validas:
        if resposta == "0": print("Saindo do programa...")
        if resposta == "/": print("Voltando ao menu anterior...")
        return resposta
    
    print("Opção inválida")
    return ""