from pyexpat.errors import messages

from config.settings import client, model_name


def classify_text(text):
    categories = [ "art", "science", "sports", "economics", "education", "entertainment", "environment", "politics", "health", "technology"]
    prompt = f"Please classify the following text: '{text}' into one of these categories: {', '.join(categories)} . The category is: "
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