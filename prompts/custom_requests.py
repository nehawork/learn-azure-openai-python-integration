from config.settings import client, model_name

# ChatGPT Request Customization
'''
Step 1: Temperature
Step 2: Max Tokens
Step 3: No of Responses
'''

def customized_prompt(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model=model_name,
        temperature=0.6,
        n=3,
        max_tokens=10,
    )

    for idx, choice in enumerate(response.choices):
        print(f"\n\n\n{idx+1}\n")
        print(choice.message.content)
