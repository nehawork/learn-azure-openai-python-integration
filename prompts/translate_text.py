from pyexpat.errors import messages

from config.settings import client, model_name


def translate_text(text, language):
    prompt = f"Please translate the following text: '{text}' to {language}. "
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content":prompt},
        ],
        n=1,
        temperature=0.5
    )
    return response.choices[0].message.content