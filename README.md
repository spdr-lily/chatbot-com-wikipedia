# **Projeto de Chatbot com Integração Wikipedia e Análise de Sentimentos**

## **1\. Introdução**

Este documento detalha o projeto de um chatbot que interage com usuários, fornecendo informações da Wikipedia e analisando o sentimento de suas mensagens. O objetivo principal é criar um sistema de conversação que seja informativo e capaz de adaptar suas respostas ao estado emocional do usuário. O projeto utiliza várias bibliotecas de processamento de linguagem natural (PLN) para alcançar esses objetivos.

## **2\. Contexto**

A criação de um chatbot com integração Wikipedia e análise de sentimentos é relevante pois permite:

* **Acesso rápido à informação:** Fornecer respostas informativas e relevantes às perguntas dos usuários utilizando o vasto conhecimento da Wikipedia.  
* **Interação personalizada:** Adaptar o estilo e o tom das respostas do chatbot com base no sentimento do usuário, tornando a interação mais natural e empática.  
* **Automatização do suporte:** Automatizar o atendimento ao cliente ou fornecer suporte informativo 24/7.  
* **Engajamento do usuário:** Criar uma experiência de usuário mais interativa e envolvente.

## **3\. Conjunto de Dados**

Este projeto não utiliza um conjunto de dados tradicional no sentido de um arquivo de dados estruturado. Em vez disso, ele utiliza as seguintes fontes e recursos:

* **Wikipedia:** A biblioteca wikipedia é usada para acessar dinamicamente o conteúdo da Wikipedia em português. As informações são buscadas e processadas em tempo real, com base nas consultas do usuário.  
* **Modelos de PLN Pré-treinados:** Modelos de análise de sentimentos da biblioteca transformers (Hugging Face) são utilizados para processar e analisar o sentimento das mensagens do usuário.  
* **Léxico VADER:** O léxico VADER (Valence Aware Dictionary and sEntiment Reasoner) do NLTK é usado para análise de sentimentos.

## **4\. Metodologia**

A metodologia do projeto envolve as seguintes etapas principais:

1. **Instalação e Importação de Bibliotecas:** As bibliotecas necessárias (wikipedia, nltk, textblob, transformers, random) são instaladas e importadas.  
2. **Configuração Inicial:** Recursos do NLTK (como o léxico VADER) são baixados, a Wikipedia é configurada para o idioma português e os modelos de análise de sentimentos são carregados.  
3. **Análise de Sentimentos:** A função analyze\_sentiment() processa a entrada do usuário para determinar seu sentimento usando TextBlob, VADER e um modelo do transformers.  
4. **Geração de Respostas do Chatbot:** A função chatbot\_response() gera respostas apropriadas com base no sentimento analisado.  
5. **Busca de Informações na Wikipedia:** A função fetch\_wikipedia\_info() busca e retorna informações relevantes da Wikipedia.  
6. **Loop de Interação:** A função main() controla o fluxo principal da conversa entre o usuário e o chatbot.

## **5\. Funções e Implementações**

### **5.1 Importação de Bibliotecas**

As seguintes bibliotecas foram importadas no início do projeto:

* nltk: Utilizada para tarefas de PLN, como análise de sentimentos (VADER).  
* textblob: Utilizada para análise de sentimentos simples.  
* transformers: Utilizada para carregar modelos pré-treinados de PLN para análise de sentimentos.  
* random: Utilizada para escolher respostas aleatórias de listas predefinidas.  
* wikipedia: Utilizada para acessar informações da Wikipedia.

### **5.2 Configuração Inicial**

Recursos e modelos necessários são inicializados:

* O léxico VADER do NLTK é baixado.  
* A Wikipedia é configurada para português (wikipedia.set\_lang("pt")).  
* O modelo de análise de sentimentos é carregado usando pipeline do transformers.

### **5.3 Função analyze\_sentiment(user\_input)**

Esta função analisa o sentimento da entrada do usuário:

* Calcula a polaridade usando TextBlob.  
* Calcula a polaridade composta usando VADER.  
* Obtém a pontuação de sentimento usando o modelo do transformers.  
* Combina as pontuações para obter um sentimento final.

### **5.4 Função chatbot\_response(user\_input)**

Esta função gera uma resposta do chatbot:

* Analisa o sentimento da entrada do usuário.  
* Seleciona aleatoriamente uma resposta apropriada de listas predefinidas (positiva, neutra, ligeiramente negativa, negativa).

### **5.5 Função fetch\_wikipedia\_info(query)**

Esta função busca informações na Wikipedia:

* Pesquisa a consulta usando wikipedia.search().  
* Obtém o resumo da página mais relevante usando wikipedia.page().  
* Retorna o resumo formatado ou uma mensagem de erro se a busca falhar.

### **5.6 Função main()**

Esta função controla o loop de interação do chatbot:

* Saúda o usuário.  
* Entra em um loop que recebe a entrada do usuário.  
* Chama fetch\_wikipedia\_info() para obter informações da Wikipedia.  
* Chama chatbot\_response() para obter uma resposta ao sentimento do usuário.  
* Imprime as respostas do chatbot e solicita feedback do usuário.  
* Encerra a conversa quando o usuário digita "sair", "exit" ou "tchau".

## **6\. Resultados**

Os principais resultados do projeto incluem:

* **Chatbot Interativo:** Um chatbot capaz de manter uma conversa básica com o usuário.  
* **Integração com a Wikipedia:** Capacidade de fornecer informações relevantes da Wikipedia em resposta às perguntas do usuário.  
* **Análise de Sentimentos:** Capacidade de analisar o sentimento das mensagens do usuário e adaptar as respostas do chatbot de acordo.  
* **Feedback do Usuário:** Implementação de um sistema simples de feedback para avaliar a qualidade das respostas do chatbot.

## **7\. Conclusão**

Este projeto demonstra a criação de um chatbot que integra funcionalidades de busca na Wikipedia com análise de sentimentos. O chatbot é capaz de fornecer informações úteis e adaptar suas respostas ao estado emocional do usuário, criando uma experiência de conversação mais envolvente. As funções implementadas permitem a interação com o usuário, a busca de informações e a análise de sentimentos de forma eficaz.
