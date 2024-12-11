<202333881 윤준혁>

- GROUP 72
 다른 팀원들과 연락을 해보려고 시도했지만 팀원들 모두 연락이 닿지 않았습니다.
팀 프로젝드에 대한 의지가 없다고 판단하고 혼자서 진행하였습니다. 이 점 양해 부탁드립니다.

1. 프로젝트 개요
 - 강의나 시험공부를 할 때 강의 자료에서 더 자세히 알고싶은 내용이 있을 때
   즉각적으로 자료를 분석하고 심층적인 내용을 알 수 있도록 도와주는 프로그램이 필요함을 느낌.
 - ChatGPT를 사용하여 자료를 즉각적을 분석하고 요약해주도록 하는 프로그램 구상

2. 설치해야 할 내역
pip install openai == 0.28
pip install pytesseract (설치 후 횐경변수 설정이 필요)
pip install pillow
pip install opencv-python
pip install numpy
pip install pyautopui
pip install tkinter (보통은 python 표준 라이브러리에 포함되어 있음)
set OPENAI_API_KEY=your_openai_api_key (이 프로그램을 사용하기 위해선 openai API를 구매해야 합니다.)
파이썬은 최신 버전 사용

3. 실행 방법
 1) main.py 실행
 2) "Shift + I 키를 누르면 분석합니다"라는 창이 생성됨
 3) Shift + I를 눌러 분석을 요청
 4) gpt-4 모델을 통해 화면을 분석한 내용이 생성됨

