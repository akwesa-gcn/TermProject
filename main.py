from screen_capture import capture_screen
from chatgpt_analysis import analyze_screen_with_chatgpt
from ui_display import show_summary
import tkinter as tk

def main():
    def on_key_press(event):
        """키 입력 인식"""
        if event.state == 1 and event.keysym == 'I':  # Shift(1) + I 키 감지
            print("Shift + I 감지됨. 화면 캡처 및 분석 실행 중...")
            # 화면 캡처
            screen_text = capture_screen()
            print("화면 분석 중...")

            # ChatGPT로 분석
            analyzed_text = analyze_screen_with_chatgpt(screen_text)

            # 분석 결과를 UI로 표시
            show_summary(analyzed_text)

    # Tkinter로 창 생성
    root = tk.Tk()
    root.title("화면 캡처 및 분석")
    root.geometry("300x200")

    # 설명 창
    label = tk.Label(root, text="Shift + I 키를 누르면 분석합니다.", wraplength=250)
    label.pack(pady=50)

    # 키 이벤트 바인딩
    root.bind("<KeyPress>", on_key_press)

    # Tkinter 이벤트 루프 실행
    root.mainloop()

if __name__ == "__main__":
    main()

