import random
from .sentiment import analyze_sentiment
from .wikipedia_search import fetch_wikipedia_info

positive_responses = [
    "Isso é ótimo! Como posso ajudar ainda mais?",
    "Fico feliz em saber disso! O que mais posso fazer por você?",
    "Que notícia maravilhosa! Conte-me mais.",
]

neutral_responses = [
    "Entendi. Você pode me contar mais?",
    "Interessante! Quer compartilhar mais detalhes?",
    "Ok! Como posso ajudar?",
]

slightly_negative_responses = [
    "Parece que algo está te incomodando. Quer me contar mais?",
    "Sinto que há algo errado. Como posso ajudar?",
    "Se precisar desabafar, estou aqui para ouvir.",
]

negative_responses = [
    "Sinto muito por isso. Como posso ajudar a melhorar seu dia?",
    "Parece que você não está tendo um bom dia. Quer conversar mais sobre isso?",
    "Lamento ouvir isso. Estou aqui para ajudar, se precisar.",
]


def chatbot_response(user_input: str) -> str:
    sentiment = analyze_sentiment(user_input)

    if sentiment > 0.5:
        return random.choice(positive_responses)
    elif sentiment > 0.1:
        return random.choice(neutral_responses)
    elif sentiment > -0.3:
        return random.choice(slightly_negative_responses)
    else:
        return random.choice(negative_responses)


def process_message(user_input: str) -> dict:
    wiki_info = fetch_wikipedia_info(user_input)
    sentiment = analyze_sentiment(user_input)
    response = chatbot_response(user_input)

    return {
        "user_input": user_input,
        "wiki_response": wiki_info,
        "sentiment_response": response,
        "sentiment_score": sentiment,
    }


def main():
    print("Chatbot: Olá! Como posso te ajudar hoje?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "tchau"]:
            print("Chatbot: Até mais! Tenha um ótimo dia.")
            break

        wiki_response = fetch_wikipedia_info(user_input)
        print("Chatbot:", wiki_response)

        feedback = input("O que achou da resposta?\n")
        from .sentiment import sentiment_pipeline
        sentimento = sentiment_pipeline(feedback)

        if sentimento[0]['label'] == "positive" and sentimento[0]['score'] > 0.6:
            print("Chatbot: Fico feliz que tenha gostado da resposta!")
        elif sentimento[0]['label'] == "negative" and sentimento[0]['score'] > 0.6:
            print("Chatbot: Que pena que não gostou da resposta. Gostaria de tentar uma outra pergunta?")
        else:
            print("Chatbot: Obrigado pelo feedback, volte sempre.")


if __name__ == "__main__":
    main()
