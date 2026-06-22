import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from src.chatbot.chatbot import process_message, analyze_sentiment
from src.chatbot.wikipedia_search import search_wikipedia, get_page_summary

st.set_page_config(page_title="Chatbot Wikipedia", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .chat-bubble-user {
        background-color: #DCF8C6;
        padding: 10px 15px;
        border-radius: 18px 18px 0 18px;
        margin: 5px 0;
        max-width: 70%;
        float: right;
        clear: both;
    }
    .chat-bubble-bot {
        background-color: #F1F0F0;
        padding: 10px 15px;
        border-radius: 18px 18px 18px 0;
        margin: 5px 0;
        max-width: 70%;
        float: left;
        clear: both;
    }
    .sentiment-positive { color: #28a745; font-weight: bold; }
    .sentiment-neutral { color: #ffc107; font-weight: bold; }
    .sentiment-negative { color: #dc3545; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Chatbot com Wikipedia e Análise de Sentimentos")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Conversa")

    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.sentiment_history = []

    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-bubble-bot">{msg["content"]}</div>', unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Digite sua mensagem:", placeholder="Pergunte algo sobre qualquer assunto...")
        submitted = st.form_submit_button("Enviar")

    if submitted and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        result = process_message(user_input)
        st.session_state.sentiment_history.append({
            "mensagem": user_input[:50] + ("..." if len(user_input) > 50 else ""),
            "score": result["sentiment_score"]
        })

        resposta = f"**Sentimento:** {result['sentiment_response']}\n\n**Wikipedia:** {result['wiki_response']}"
        st.session_state.messages.append({"role": "bot", "content": resposta})
        st.rerun()

with col2:
    st.subheader("📊 Análise em Tempo Real")

    if st.session_state.sentiment_history:
        df = pd.DataFrame(st.session_state.sentiment_history)

        ultimo_score = df["score"].iloc[-1]
        if ultimo_score > 0.3:
            label = "Positivo 😊"
            color = "#28a745"
        elif ultimo_score > -0.3:
            label = "Neutro 😐"
            color = "#ffc107"
        else:
            label = "Negativo 😞"
            color = "#dc3545"

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=ultimo_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"Sentimento: {label}", 'font': {'size': 16, 'color': color}},
            number={'suffix': "", 'font': {'color': color, 'size': 24}},
            gauge={
                'axis': {'range': [-1, 1], 'tickvals': [-1, -0.5, 0, 0.5, 1],
                         'ticktext': ["-1", "-0.5", "0", "0.5", "1"]},
                'bar': {'color': color, 'thickness': 0.3},
                'steps': [
                    {'range': [-1, -0.3], 'color': "#f8d7da"},
                    {'range': [-0.3, 0.3], 'color': "#fff3cd"},
                    {'range': [0.3, 1], 'color': "#d4edda"},
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': ultimo_score
                }
            }
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

        if len(df) > 1:
            fig_line = px.line(df, x=df.index, y="score",
                               title="Histórico de Sentimentos",
                               labels={"index": "Mensagem", "score": "Score"},
                               markers=True)
            fig_line.update_traces(line=dict(color="#6f42c1", width=3),
                                   marker=dict(size=10, color=df["score"].apply(
                                       lambda x: "#28a745" if x > 0.3 else "#ffc107" if x > -0.3 else "#dc3545")))
            fig_line.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("👆 Envie uma mensagem para ver a análise de sentimentos aqui.")

st.markdown("---")

st.subheader("🔍 Pesquisa Direta na Wikipedia")
col_search1, col_search2 = st.columns([3, 1])
with col_search1:
    search_term = st.text_input("Termo para pesquisar na Wikipedia:")
with col_search2:
    search_button = st.button("Pesquisar", key="wiki_search")

if search_button and search_term:
    with st.spinner("Buscando na Wikipedia..."):
        results = search_wikipedia(search_term)
        if results:
            st.success(f"Encontrados {len(results)} resultados:")
            for i, title in enumerate(results, 1):
                with st.expander(f"{i}. {title}"):
                    summary = get_page_summary(title)
                    st.write(summary[:500] + "..." if len(summary) > 500 else summary)
        else:
            st.warning("Nenhum resultado encontrado.")

st.markdown("---")
st.markdown("Desenvolvido com Python, Streamlit, Wikipedia API, Transformers & NLTK")
