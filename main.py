from prompts.basic_prompts import list_models, basic_chat
from prompts.custom_requests import customized_prompt
from analysis.response_analyzer import analyze_response

if __name__ == "__main__":
    list_models()

    print("\n=== Basic Prompt ===\n")
    basic_chat("Write a poem on python")

    print("\n=== Custom Request ===\n")
    customized_prompt("Choose a good name for elephant")

    print("\n=== Analyze Story ===\n")
    analyze_response("Write a short story about trip to bali")
