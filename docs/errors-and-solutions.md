# Erros Comuns e Soluções

## 1. Erro: `wikipedia.exceptions.DisambiguationError`

**Causa:** O termo pesquisado retorna múltiplos resultados (ex: "Python" pode ser a linguagem ou a cobra).

**Solução:**
- O código já captura esse erro e sugere opções mais específicas.
- Seja mais específico na consulta (ex: "Python linguagem" em vez de "Python").

## 2. Erro: `wikipedia.exceptions.PageError`

**Causa:** O termo pesquisado não corresponde a nenhuma página da Wikipedia.

**Solução:**
- Verifique a ortografia do termo pesquisado.
- Tente usar sinônimos ou termos mais genéricos.

## 3. Erro: `requests.exceptions.ConnectionError` / `TimeoutError`

**Causa:** Sem conexão com a internet ou a Wikipedia está inacessível.

**Solução:**
- Verifique sua conexão com a internet.
- Aguarde e tente novamente.
- Configure um timeout maior se estiver em uma rede lenta.

## 4. Erro: `ModuleNotFoundError: No module named 'transformers'`

**Causa:** Dependências não instaladas.

**Solução:**
```bash
pip install -r requirements.txt
```

## 5. Erro: `OSError: Can't load tokenizer for 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'`

**Causa:** O modelo Transformer não foi baixado ou o cache está corrompido.

**Solução:**
```bash
pip install --upgrade transformers
python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='lxyuan/distilbert-base-multilingual-cased-sentiments-student')"
```

## 6. Erro: `LookupError: NLTK resource vader_lexicon not found`

**Causa:** O recurso VADER do NLTK não foi baixado.

**Solução:**
```python
import nltk
nltk.download('vader_lexicon')
```

## 7. Erro de memória ao carregar modelo Transformer

**Causa:** O modelo requer mais RAM do que está disponível.

**Solução:**
- Use um modelo menor (ex: `'cardiffnlp/twitter-roberta-base-sentiment-latest'`)
- Feche outros programas para liberar memória.
- No Docker, aumente o limite de memória em `docker-compose.yml`.

## 8. Streamlit: `RuntimeError: Cannot run multiple Streamlit sessions`

**Causa:** Tentativa de executar múltiplas instâncias do Streamlit no mesmo processo.

**Solução:**
- Feche todas as abas do navegador com o app.
- Use `st.rerun()` em vez de `st.experimental_rerun()`.
- Reinicie o servidor.

## 9. Erro: `FileNotFoundError: [Errno 2] No such file or directory: 'data/...'`

**Causa:** O diretório `data/` não existe ou o caminho está incorreto.

**Solução:**
- Verifique se está executando do diretório raiz do projeto.
- Use caminhos absolutos com `os.path.join()`.

## 10. Docker: `port is already allocated`

**Causa:** A porta 8501 já está em uso.

**Solução:**
```bash
# Parar container anterior
docker compose down
# Ou usar porta diferente
docker run -p 8502:8501 chatbot-wikipedia
```

## 11. Erro: `ImportError: cannot import name 'pipeline' from 'transformers'`

**Causa:** Versão desatualizada da biblioteca transformers.

**Solução:**
```bash
pip install --upgrade transformers
```

## 12. Sentimento sempre neutro

**Causa:** O modelo pode não estar capturando sentimento em português corretamente.

**Solução:**
- O modelo `'lxyuan/distilbert-base-multilingual-cased-sentiments-student'` suporta português.
- Verifique se o texto tem palavras com carga emocional clara.
- Teste com frases como "Eu estou muito feliz!" ou "Estou triste hoje."

## 13. O Docker não encontra o arquivo `app.py`

**Causa:** O contexto de build do Docker não inclui o diretório correto.

**Solução:**
```dockerfile
COPY . .
# Certifique-se de que app.py está no diretório raiz do projeto
```

## 14. Resposta da Wikipedia muito longa

**Causa:** O resumo da Wikipedia pode ser extenso para alguns tópicos.

**Solução:**
- O código já usa `page.summary` que retorna apenas o resumo.
- Para limitar ainda mais, use `texto.summary[:500]`.

## 15. Erro no Windows: `OSError: [WinError 127] ...`

**Causa:** Problema de compatibilidade com certas bibliotecas no Windows.

**Solução:**
- Use WSL2 (Windows Subsystem for Linux) para executar o projeto.
- Ou use o Docker (recomendado).

## Dicas de Debug

### Verificar dependências instaladas:
```bash
pip list | findstr /I "wikipedia nltk textblob transformers streamlit"
```

### Testar conexão com Wikipedia:
```python
import wikipedia
wikipedia.set_lang("pt")
print(wikipedia.summary("Brasil"))
```

### Testar análise de sentimento:
```python
from src.chatbot.sentiment import analyze_sentiment
print(analyze_sentiment("Eu amo este projeto!"))
```

### Verificar logs do Docker:
```bash
docker compose logs -f
```
