import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()                                   # loads .env into environment
my_api_key = os.getenv("GROQ_API_KEY")          # name must match your .env

if not my_api_key:
    raise ValueError("API key not found")       

client = Groq(api_key=my_api_key)               # register as client
model = "openai/gpt-oss-120b"               # exact model name

# models
# openai/gpt-oss-120b
# openai/gpt-oss-20b
# qwen/qwen3.8-27b

message = {"role": "user", "content": "what is the meaning of the name Tufail?"}
messages = [message]                            # always a list

response = client.chat.completions.create(
    model=model,
    messages=messages,
)

# print(response)                                 # full response
print(response.choices[0].message.content)      # the actual answer