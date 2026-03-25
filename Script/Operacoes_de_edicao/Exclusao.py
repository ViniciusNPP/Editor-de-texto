import os
import re
import Aparencia.ap_excluir as ap_ex

def ExcluirNormal(texto):
    proc = ap_ex.AparenciaExclusaoNormal()
    
    if proc != "":
        return texto.replace(proc, "")
    return texto

def ExcluirSequencia(texto):
    print()