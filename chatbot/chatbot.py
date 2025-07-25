from prompts.chatbot_requests import ask_chatbot
from prompts.response_relevance_check import is_relevant


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

    # Filter Answers - Forbidden Words
    '''
    Step 1 - Setting Variables
    Step 2 - Filtering Forbidden Words
    Step 3 - Intercepting the response
    '''
    forbidden_words = ['the', 'and', 'for', 'you', 'are', 'not']

    '''
    Check response relevance

    Step 1: Calculate Similarities
    Step 2: Vectorize Text
    Step 3: Adapt the response
    '''

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
        chatbot_answer = ask_chatbot(history, forbidden_words)
        relevant = is_relevant(chatbot_answer, user_input)

        if relevant:
            print(f"{chatbot_answer}")
            prev_questions.append(user_input)
            prev_answers.append(chatbot_answer)
        else:
            print("Answer is not relevant, please try again.")
