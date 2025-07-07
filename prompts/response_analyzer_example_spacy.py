import spacy
from config.settings import client, model_name

model_spacy = spacy.load("en_core_web_md")

# Process & Analyze ChatGPT Response
'''
Step 1: Analyze the answer
Step 2: Use the extracted information

To analyze the answer, there are libraries available in python
spaCy, TextBlob, NLTK
'''

def analyze_response_example_spacy(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        n=5,
        max_tokens=200,
    )

    for idx, choice in enumerate(response.choices):
        print(f"\n\n\n{idx+1}\n")
        content = choice.message.content
        print(content)

        print("\n\n***Analysis***\n")
        analysis = model_spacy(content)

        print("\n*Token*\n")
        for token in analysis:
            print(f"{token.text} | {token.pos_} | {token.dep_} | {token.head.text} | {token.head.pos_}\n")

        print("\n*Entities*\n")
        for ent in analysis.ents:
            print(f"{ent.text} | {ent.label_}\n")
            if ent.label_ == "LOC":
                print(f"\nMore about location: {ent.text}\n")
                fetch_more_about_location(ent.text)

def fetch_more_about_location(location):
    prompt = f"Tell me more about {location}"
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        n=1,
        max_tokens=100,
    )
    print(response.choices[0].message.content)
