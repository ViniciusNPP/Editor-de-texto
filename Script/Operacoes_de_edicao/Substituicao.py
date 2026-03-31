import re
import os
import time
import Aparencia.ap_substituir as ap_sub

def SubstituirNormal(texto):
    os.system("cls")
    
    proc, subst = ap_sub.AparenciaSubNormal()
    
    return texto.replace(proc, subst)

def SubstituirSequencia(texto):
    os.system("cls")
    
    proc, subst = ap_sub.AparenciaSubSequencia()
    
    #Separação dos termos a ser procurados em um dicionário
    dicionario_sub = {
        proc[i]: subst[i] if i < len(subst) else subst[-1]
        for i in range(len(proc))
    }

    #Substituindo no texto as chaves do dicionário pelos seus valores
    padrao = re.compile("|".join(re.escape(k) for k in dicionario_sub.keys()))
    return padrao.sub(lambda x: dicionario_sub[x.group(0)], texto)

def SubstituirRegex(texto):
    proc, subst = ap_sub.AparenciaSubRegex()
    
    #Criação do dicionário para armazenar os grupos e seus valores
    dicionario_sub = {
        f"g{i}": (subst[i] if i < len(subst) else subst[-1]) #Cria a chave com o nome do grupo e atribui o valor correspondente.
        for i in range(len(proc))
    }
    
    #Função para indiciar qual chave/ grupo foi achado no texto e retornar o valor correspondente
    def SubstituirRegexFunc(match):
        grupo = match.lastgroup
        return dicionario_sub[grupo]
    
    #Substituição das chaves pelos seus valores
    padrao = re.compile("|".join(f"(?P<g{i}>{r})" for i, r in enumerate(proc)))
    return padrao.sub(SubstituirRegexFunc, texto)
    