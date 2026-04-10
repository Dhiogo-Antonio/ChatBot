sinonimos = {
    "oi": ["ola", "eai", "opa", "salve"],
    "ajuda": ["socorro", "suporte", "help", "auxilio"],
    "problema": ["erro", "bug", "falha", "defeito"],
    "nome": ["quem é você", "como se chama"],
    "tchau": ["adeus", "falou", "até mais"],
    "como": ["como faço", "de que forma"],
    "quando": ["que horas", "qual horario"]
}



intencoes = {
    "saudacao": {
        "palavras": ["oi", "ola", "eai", "opa", "bom dia", "boa tarde", "boa noite"],
        "respostas": [
            "Olá! Como posso ajudar?",
            "Oi! Tudo bem?",
            "E aí! No que posso te ajudar?"
        ]
    },

    "despedida": {
        "palavras": ["tchau", "adeus", "falou", "até mais"],
        "respostas": [
            "Até mais!",
            "Tchau! Volte sempre."
        ]
    },

    "nome": {
        "palavras": ["nome", "quem é você", "como se chama"],
        "respostas": [
            "Sou uma IA desenvolvida em Python.",
            "Você pode me chamar de assistente virtual."
        ]
    },

    "capacidade": {
        "palavras": ["o que você faz", "para que serve"],
        "respostas": [
            "Posso responder perguntas, ajudar com problemas e aprender com você."
        ]
    },

    "ajuda": {
        "palavras": ["ajuda", "socorro", "suporte", "help"],
        "respostas": [
            "Claro, como posso te ajudar?",
            "Me diga o que você precisa."
        ]
    },

    "problema": {
        "palavras": ["erro", "bug", "problema", "falha"],
        "respostas": [
            "Pode descrever melhor o problema?",
            "Quando isso acontece?"
        ]
    },

    "como_fazer": {
        "palavras": ["como", "como faço", "como criar", "como usar"],
        "respostas": [
            "Pode ser mais específico sobre o que você quer fazer?"
        ]
    },

    "explicacao": {
        "palavras": ["o que é", "explique", "defina", "significa"],
        "respostas": [
            "Você pode especificar melhor o que deseja entender?"
        ]
    },

    "tempo": {
        "palavras": ["quando", "que horas", "qual horario"],
        "respostas": [
            "Pode detalhar melhor sua pergunta sobre tempo?"
        ]
    },

    "opiniao": {
        "palavras": ["o que acha", "sua opinião"],
        "respostas": [
            "Depende do contexto, pode explicar melhor?"
        ]
    }
}