import re
import os
import Aparencia.ap_substituir as ap_sub

def SubstituirNormal(texto):
    os.system("cls")
    
    proc, subst = ap_sub.AparenciaSubNormal()
    
    return texto.replace(proc, subst)

def SubstituirSequencia(texto):
    os.system("cls")
    
    proc, subst = ap_sub.AparenciaSubSequencia()
    
    #Separação dos termos a ser procurados em um dicionário
    dicionario_sub = dict.fromkeys(proc.split(", "), "")
    
    #Atribuição dos valores as chaves do dicionário
    subst = subst.split(", ")
    tamanho_subst = len(subst)
    j = 0
    
    for i in dicionario_sub:
        if j < tamanho_subst:
            dicionario_sub[i] = subst[j]
            j += 1
        else:
            dicionario_sub[i] = subst[-1]

    #Substituindo no texto as chaves do dicionário pelos seus valores
    padrao = re.compile("|".join(re.escape(k) for k in dicionario_sub.keys()))
    resultado = padrao.sub(lambda x: dicionario_sub[x.group(0)], texto)
    
    return resultado

def SubstituirRegex(texto):
    proc, subst = ap_sub.AparenciaSubRegex()
    
    padrao = re.compile(proc)
    resultado = padrao.sub(subst, texto)
    
    return resultado