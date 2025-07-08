from config.settings import client, model_name
from prompts.filter_words import black_list_filter


def ask_chatbot(prompt, black_list):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        temperature=1.5,
        n=1,
        max_tokens=150,
    )

    uncontrolled_response = response.choices[0].message.content
    controlled_response = black_list_filter(uncontrolled_response, black_list)
    return controlled_response