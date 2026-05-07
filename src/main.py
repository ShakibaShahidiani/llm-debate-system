from dotenv import load_dotenv
import os
import litellm
from litellm import completion


litellm._turn_on_debug()

# Load API keys from .env file
load_dotenv()

# Test message to groq
response = completion(
    model = "groq/llama-3.1-8b-instant",
    messages = [
        {"role" : "user", "content" : "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)