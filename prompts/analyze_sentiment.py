from pyexpat.errors import messages

from config.settings import client, model_name


def analyze_sentiment(text):
    prompt = f"Please analyze the sentiment of the following text: '{text}'. The sentiment is: "
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content":prompt},
        ],
        n=1,
        max_tokens=50,
        temperature=0.5
    )
    return response.choices[0].message.content