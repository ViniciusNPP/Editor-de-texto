import re
import Aparencia.ap_excluir as ap_ex

def ExcluirNormal(texto):
    proc = ap_ex.AparenciaExclusaoNormal()
    
    if proc != "":
        return texto.replace(proc, "")
    return texto

def ExcluirSequencia(texto):
    proc = ap_ex.AparenciaExclusaoSequencia()
    
    if proc != "":
        padrao = re.compile("|".join(re.escape(i) for i in proc.split(", ")))
        resultado = padrao.sub("", texto)
        
        return resultado
    return texto

def ExcluirRegex(texto):
    proc = ap_ex.AparenciaExclusaoRegex()
    
    if proc != "":
        padrao = re.compile(proc)
        resultado = padrao.sub("", texto)
        
        return resultado
    return texto