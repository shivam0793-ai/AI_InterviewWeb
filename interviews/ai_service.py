from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client=Groq(api_key=os.getenv('GROQ_API_KEY'))
model=os.getenv('GROQ_MODEL')

def chat_with_ai(history,user_msg):
    message=[
        {'role':'system',
         'content':("You are a professional AI interviewer. "
                "Ask one interview question at a time. "
                "After each answer give short feedback and ask the next question.")}
    ]

    for msg in history:
        message.append({'role':msg['role'],
                        'content':msg['text']})

    message.append(
        {'role':'user',
        'content':user_msg}
    )

    respone=client.chat.completions.create(
        model=model,
        messages=message,
        temperature=0.7,
        max_completion_tokens=500
    )

    return respone.choices[0].message.content