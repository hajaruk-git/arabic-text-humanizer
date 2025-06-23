from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def my_gpt(prompt):
    messages = [
    {
        "role": "system",
        "content": "أنت مساعد لغوي صارم. لا يُسمح لك باستخدام أي لهجة عربية على الإطلاق. هذا يشمل: المصرية، الشامية، الخليجية، المغاربية، أو أي لهجة أخرى. يُسمح فقط باستخدام اللغة العربية الفصحى البسيطة والواضحة. لا تكتب أبدًا كلمات مثل: اللي، مو، صار، عشان، إلخ. أي استخدام للهجة يعتبر خطأ. يجب أن تكتب بأسلوب فصيح فقط، حتى وإن كان بسيطًا."
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