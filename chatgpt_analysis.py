import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_screen_with_chatgpt(screen_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # "gpt-3.5-turbo"로 변경 가능
            messages=[
                {"role": "system", "content": "당신은 학생 역할을 수행하는 AI 비서입니다."},
                {"role": "user", "content": screen_text},
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:  # 모든 예외 처리
        print(f"OpenAI API 호출 중 오류 발생: {e}")
        return "화면 분석 중 오류가 발생했습니다."
