import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import json
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

text = """Hello, my name is Pratyush. I purchased an iPhone which stopped working. My address is Delhi. My father's name is ... Please contact me at abc@gmail.com"""

prompt = f"""This is a customer ticket. Please extract the personal information.
{text}"""

schema = Ticket.model_json_schema()
response_format = {"type": "json_object"}

system_prompt = f"""Extract the information and return it in JSON format
matching this schema: {schema}"""

system_message = {"role": "system", "content": system_prompt}
user_message   = {"role": "user",   "content": prompt}

messages = [system_message, user_message]          # system first


response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format,
)

answer = response.choices[0].message.content

raw_json = answer
data_file = json.loads(raw_json)       # JSON string -> Python dict
ticket = Ticket(**data_file)           # dict -> Ticket object


print(ticket.name)
print(ticket.email)
print(ticket.issue)

print(ticket)
