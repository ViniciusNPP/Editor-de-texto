def OpcoesValidas(resposta, opcoes_validas):
    if resposta in opcoes_validas:
        if resposta == "0": print("Saindo do programa...")
        if resposta == "/": print("Voltando ao menu anterior...")
        return resposta
    
    print("Opção inválida")
    return ""

def NumerosRomanos(numero):
    if not numero.isdigit():
        return numero
    
    numero = int(numero)
    resultado = ""
    
    num_romanos = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    
    while numero > 0:
        for valor in num_romanos.keys():
            if numero >= valor:
                resultado += num_romanos[valor]
                numero -= valor
                break
    
    return resultado
