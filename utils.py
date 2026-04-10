import unicodedata

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto.strip()


def resumir(texto, limite=300):
    if len(texto) > limite:
        return texto[:limite] + "..."
    return texto