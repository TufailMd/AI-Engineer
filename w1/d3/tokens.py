import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

prompt1 = "Hi"
prompt2 = "Explain time travel in detail"
prompt3 = "Write a 1000 word essay on machine learning"

prompts = [prompt1, prompt2, prompt3]      # a list of prompts

for prompt in prompts:
    message = {"role": "user", "content": prompt}
    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=50,                      # limit the reply length
    )

    usage = response.usage
    print("Prompt:", prompt)
    print("Prompt tokens:", usage.prompt_tokens)
    print("Completion tokens:", usage.completion_tokens)
    print("Total tokens:", usage.total_tokens)
    print("Finish reason:", response.choices[0].finish_reason)