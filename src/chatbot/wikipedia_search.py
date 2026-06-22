import wikipedia

wikipedia.set_lang("pt")


def fetch_wikipedia_info(query: str) -> str:
    try:
        resultados = wikipedia.search(query)
        if not resultados:
            return "Desculpe, não encontrei informações sobre esse assunto."
        melhor_resultado = resultados[0]
        texto = wikipedia.page(melhor_resultado)
        return f"{texto.summary}\n\nFonte: {melhor_resultado} - Wikipedia"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Múltiplos resultados encontrados: {', '.join(e.options[:5])}. Seja mais específico."
    except wikipedia.exceptions.PageError:
        return "Não foi encontrada uma página para esse termo."
    except Exception as e:
        return f"Houve um erro ao buscar informações: {str(e)}"


def search_wikipedia(query: str, max_results: int = 5) -> list:
    try:
        return wikipedia.search(query, results=max_results)
    except Exception:
        return []


def get_page_summary(title: str) -> str:
    try:
        page = wikipedia.page(title)
        return page.summary
    except Exception:
        return ""
