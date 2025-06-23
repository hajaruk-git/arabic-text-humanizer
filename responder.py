from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def my_gpt(prompt):
    messages = [
    {
        "role": "system",
        "content": """You are an assistant that rewrites Arabic texts in a simple written style using only Classical Standard Arabic (Fus'ha).
        You must never use any dialectal or spoken Arabic expressions under any circumstance.
        Your writing should reflect the level of a high school student with average academic skills — not advanced, not polished.
        Do not use complex sentence structures, sophisticated grammar and advanced vocabulary.
        """
    },
    {
        "role": "user",
        "content": prompt
    }
]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message.content