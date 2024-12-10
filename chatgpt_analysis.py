import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_screen_with_chatgpt(screen_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "당신은 학생 역할을 수행하는 AI 비서입니다."},
            {"role": "user", "content": screen_text},
        ]
    )
    return response['choices'][0]['message']['content']
