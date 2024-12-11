from tkinter import Tk, Label

def show_summary(summary_text):
    """
    분석된 텍스트를 UI 창에 표시 (문단 간 여백 추가).
    """
    # 문단 간 여백 추가
    formatted_text = "\n\n".join(line.strip() for line in summary_text.splitlines() if line.strip())

    # Tkinter 창 생성
    root = Tk()
    root.title("화면 분석 결과")
    root.geometry("900x1000")  # 창 크기 조정

    # 텍스트 출력
    Label(
        root,
        text=formatted_text,
        wraplength=750,  # X축으로 길게 표시되도록 wraplength 설정
        justify="left",  # 텍스트를 왼쪽 정렬
        anchor="w",  # 위쪽 왼쪽 정렬
        padx=10,
        pady=10
    ).pack()

    root.mainloop()
