import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_screen_with_chatgpt(screen_text):
    """
    캡처한 화면 텍스트를 GPT 모델로 분석.
    """
    # 상단 탭 정보 및 웹 주소 제거
    filtered_text = "\n".join(
        line for line in screen_text.splitlines()
        if not (line.startswith("http") or "://" in line or len(line.split()) == 1)
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 또는 "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": f"다음 텍스트를 분석해 주세요. 한글로 답변해 주세요:\n{filtered_text}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"OpenAI API 호출 중 오류 발생: {e}")
        return "화면 분석 중 오류가 발생했습니다."
