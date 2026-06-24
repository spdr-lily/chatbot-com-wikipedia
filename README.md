# **Chatbot com Wikipedia e Análise de Sentimentos**

Chatbot interativo que consulta a Wikipedia e analisa o sentimento das mensagens usando TextBlob, VADER (NLTK) e Transformers (Hugging Face).

## 🚀 Como Executar

### Localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Docker
```bash
docker compose up --build
```

Acesse: http://localhost:8501

## 📁 Estrutura do Projeto

```
├── streamlit_app.py                # Entry point para Streamlit Cloud
├── app.py                          # Dashboard Streamlit
├── Dockerfile                      # Imagem Docker
├── docker-compose.yml              # Orquestração Docker
├── Makefile                        # Comandos utilitários
├── requirements.txt                # Dependências
├── src/
│   └── chatbot/
│       ├── __init__.py
│       ├── sentiment.py            # Análise de sentimentos
│       ├── wikipedia_search.py     # Busca na Wikipedia
│       └── chatbot.py              # Lógica do chatbot
├── docs/
│   └── errors-and-solutions.md     # Erros comuns e soluções
├── chatbot_com_wikipedia.ipynb     # Notebook original
└── .gitignore
```

## 🧠 Funcionalidades

- **Busca na Wikipedia** em português com fallback para erros
- **Análise de sentimentos** combinando 3 modelos (TextBlob, VADER, Transformers)
- **Dashboard interativo** com visualização de sentimentos em tempo real (Streamlit + Plotly)
- **Pesquisa direta** na Wikipedia dentro do dashboard

## ☁️ Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login com seu GitHub
2. Clique em **"New app"** 
3. Selecione este repositório: `spdr-lily/chatbot-com-wikipedia`
4. Em **"Main file path"** coloque: `streamlit_app.py` (ou `app.py`)
5. Clique em **"Deploy"**

> ⚠️ A primeira execução pode levar 2-3 minutos para baixar o modelo de sentimentos do Hugging Face. Nas execuções seguintes será mais rápido.

## 🐳 Docker

```bash
docker compose up --build -d
```

## 📖 Documentação de Erros

Consulte [docs/errors-and-solutions.md](docs/errors-and-solutions.md) para soluções de problemas comuns.

## 🛠️ Tecnologias

Python, Streamlit, Wikipedia API, NLTK (VADER), TextBlob, Transformers (Hugging Face), Plotly, Docker
