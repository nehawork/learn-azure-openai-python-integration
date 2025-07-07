from config.settings import client, model_name

def list_models():
    models = client.models.list()
    for model in models:
        print(model.id)

# interact with ChatGPT from Python
'''
Step 1: Prepare the request
Step 2: Send the request
Step 3: Process and display the response
'''

def basic_chat(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        model=model_name,
    )
    print(response.choices[0].message.content)
