import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_screen_with_chatgpt(screen_text):
    """
    캡처한 화면 텍스트를 GPT 모델로 심층적으로 분석.
    """
    # 상단 탭 정보 및 웹 주소 제거
    filtered_text = "\n".join(
        line for line in screen_text.splitlines()
        if not (line.startswith("http") or ":/" in line or len(line.split()) == 1)
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"다음 텍스트를 읽고 상세하게 설명해"
                        f"텍스트에서 중요한 내용을 심층적으로 분석하고 더욱 자세하게 설명해. 파일명과 웹 주소, 북마크 등은 분석하지 마"
                        f"그리고 한글로 답변해 :\n\n{filtered_text}"
                    )
                }
            ],
            max_tokens=1500,  # 더 긴 응답을 위해 max_tokens 증가
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"OpenAI API 호출 중 오류 발생: {e}")
        return "화면 분석 중 오류가 발생했습니다."
