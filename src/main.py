from dotenv import load_dotenv
import os
import litellm
from litellm import completion


# Load API keys from .env file
load_dotenv()

def call_llm(model, persona, conversation_history):
    messages = [
        {"role":"system", "content" : persona},
    ] + conversation_history

    response = completion(
        model= model,
        messages=messages
    )

    return response.choices[0].message.content
def debate(question, models, persona, num_rounds =3):
    print(f"\nQuestion: {question}\n")
    print("=" * 50)

    conversation_history = [
        {"role": "user", "content" : question}]
    
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}:")
        print("-" * 30)

        for i, (model, persona) in enumerate(zip(models, personas)):
            response = call_llm(model, persona, conversation_history)

            print(f"\n🤖 Agent {i+1} ({model}):")
            print(response)

            conversation_history.append({
                "role" : "user",
                "content" : f"Agent {i + 1} says: {response}"
            })
    return conversation_history


if __name__ == "__main__" :
    models = [
        "groq/llama-3.1-8b-instant",
        "groq/llama-3.3-70b-versatile",
        "groq/meta-llama/llama-4-scout-17b-16e-instruct"
    ]
    personas = [
        "You are an optimistic agent. Always highlight the positive sides of any topic.",
        "You are a critical agent. Always challenge ideas and highlight risks.",
        "You are a neutral agent. Always provide balanced and objective perspectives."
    ]
    
    question = "Should artificial intelligence replace human doctors?"
    
    debate(question, models, personas)