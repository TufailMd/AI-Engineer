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

# messages = [
#     {"role": "system", "content": "You are my loving girlfriend."},
#     {"role": "user",   "content": "I love you baby"},
# ]

# response = client.chat.completions.create(
#     model=model,
#     messages=messages,
# )

# # print(response)
# print(response.choices[0].message.content)

message_system = {"role": "system", "content": "You are a brand manager who suggests names for my brand."}
message = {"role": "user", "content": "I own a food company. Suggest one name."}
messages = [message_system, message]      # system first

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1,                        # 0 to 2
)
print(response.choices[0].message.content)