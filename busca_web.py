import requests
import wikipedia

wikipedia.set_lang("pt")


def buscar_wikipedia(pergunta):
    try:
        return wikipedia.summary(pergunta, sentences=2)
    except:
        return None



def buscar_duckduckgo(pergunta):
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": pergunta,
            "format": "json",
            "lang": "pt-br"
        }

        res = requests.get(url, params=params).json()

        if res.get("Abstract"):
            return res["Abstract"]

        for item in res.get("RelatedTopics", []):
            if "Text" in item:
                return item["Text"]

        return None

    except:
        return None



def buscar_web(pergunta):
    
    resposta = buscar_wikipedia(pergunta)
    if resposta:
        return resposta

    
    resposta = buscar_duckduckgo(pergunta)
    if resposta:
        return resposta

    return None

def buscar_calculo_web(expressao):
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            "q": expressao,
            "format": "json"
        }

        res = requests.get(url, params=params).json()

        if res.get("Answer"):
            return res["Answer"]

        if res.get("Abstract"):
            return res["Abstract"]

        return None

    except:
        return None