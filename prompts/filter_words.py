import spacy

model_spacy = spacy.load("en_core_web_md")

def black_list_filter(text, black_list):
    tokens = model_spacy(text)
    result = []

    for token in tokens:
        if token.text.lower() not in black_list:
            result.append(token.text)
        else:
            result.append("[xxxx]")


    return " ".join(result)