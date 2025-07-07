from config.settings import client, model_name

def generate_content(topic, token, temperature):
    prompt = f"Please write a short article on the topic: {topic} \n"
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        temperature=temperature,
        n=1,
        max_tokens=token,
    )
    return response.choices[0].message.content


def summarize_content(text, token, temperature):
    prompt = f"Please create a summary for this article: {text} \n"
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        temperature=temperature,
        n=1,
        max_tokens=token,
    )
    return response.choices[0].message.content