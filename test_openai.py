import openai

# OpenAI API 키 설정
openai.api_key = "your_openai_api_key"

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "테스트 메시지"},
            {"role": "user", "content": "안녕하세요, OpenAI GPT-4 테스트입니다."},
        ],
        max_tokens=50,  # 응답 토큰 수 제한
        temperature=0.7  # 창의성 정도 설정
    )
    print("API 호출 성공:", response["choices"][0]["message"]["content"])
except openai.error.OpenAIError as e:
    print(f"API 호출 중 오류 발생: {e}")
