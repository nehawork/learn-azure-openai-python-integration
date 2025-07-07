from chatbot.chatbot import init_chatbot
from prompts.analyze_sentiment import analyze_sentiment
from prompts.basic_prompts import list_models, basic_chat
from prompts.classify_text import classify_text
from prompts.content_prompts import generate_content, summarize_content
from prompts.custom_requests import customized_prompt
from prompts.response_analyzer_example_spacy import analyze_response_example_spacy
from prompts.translate_text import translate_text

if __name__ == "__main__":
    list_models()

    print("\n=== Basic Prompt ===\n")
    basic_chat("Write a poem on python")

    print("\n=== Custom Request ===\n")
    customized_prompt("Choose a good name for elephant")

    print("\n=== Analyze Story ===\n")
    analyze_response_example_spacy("Write a short story about trip to bali")

    print("\n=== Chatbot ===\n")
    init_chatbot()

    print("\n=== Generate Content ===\n")
    topic = input("Please enter a topic for your article: ")
    tokens = int(input("How many maximum token the article will have? : "))
    temperature = int(input("From 1 to 10, how creative you want the article to be?")) / 10

    generatedText = generate_content(topic, tokens, temperature)
    print(generatedText)

    print("\n=== Summaries Content ===\n")
    original_article = input("Please paste the article you want to summarize: (Please delete all the jumplines)")
    summary_tokens = int(input("How many maximum token the summary will have? : "))
    summary_temperature = int(input("From 1 to 10, how creative you want the summary to be?")) / 10

    generatedSummary = summarize_content(original_article, summary_tokens, summary_temperature)
    print(generatedSummary)

    print("\n=== Analyze Sentiment ===\n")
    text_toanalyze = input("Write your text: ")
    sentiment = analyze_sentiment(text_toanalyze)
    print(sentiment)

    print("\n=== Classify Text ===\n")
    text_toclassify = input("Write your text: ")
    classification_result = classify_text(text_toclassify)
    print(f"Classified Category is {classification_result}")

    print("\n=== Translate Text ===\n")
    text_totranslate = input("Write your text: ")
    language = input("In which language you want to translate?")
    translated_text = translate_text(text_totranslate, language)
    print(translated_text)


