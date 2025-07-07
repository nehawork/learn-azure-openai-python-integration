from prompts.chatbot_requests import ask_chatbot


def init_chatbot():
    print("Welcome to the chatbot. Write 'exit' to finish the chat. Write 'clear' to clear the contexts & history.")

    '''
    Maintain Context in Chatbot Conversations

    Step 1: Create the variables
    Step 2: Store the conversations
    Step 3: Create functionality

    '''
    prev_questions = []
    prev_answers = []
    history = ''

    while True:
        user_input = input("\nYou:")
        if user_input == "exit":
            break
        if user_input == "clear":
            prev_questions=[]
            prev_answers=[]
            history = ''
            print("Context and history has been cleared. You can continue with to chatbot with fresh context.")
            continue

        for question, answer in zip(prev_questions, prev_answers):
            history += f"The user asks: {question}"
            history += f"Chatbot answers: {answer}"

        prompt = f"The user asks: {user_input} \n"
        history += prompt
        chatbot_answer = ask_chatbot(history)
        print(f"{chatbot_answer}")
        prev_questions.append(user_input)
        prev_answers.append(chatbot_answer)
