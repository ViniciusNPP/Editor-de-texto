import fitz as pdf
    
def LerTxt(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        return file.read()
    
def LerPdf(arquivo):
    pdf_doc = pdf.open(arquivo)
    texto = ""
    
    for page in pdf_doc:
        texto += page.get_text()
    
    pdf_doc.close()
    return texto