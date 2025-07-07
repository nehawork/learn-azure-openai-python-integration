from config.settings import client, model_name

def ask_chatbot(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        temperature=1.5,
        n=1,
        max_tokens=150,
    )

    return response.choices[0].message.content
