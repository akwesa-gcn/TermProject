from tkinter import Tk, Label

def show_summary(summary_text):
    """
    분석된 텍스트를 UI 창에 표시
    """
    # 문단 간 여백
    formatted_text = "\n\n".join(line.strip() for line in summary_text.splitlines() if line.strip())

    # Tkinter 창 생성
    root = Tk()
    root.title("화면 분석 결과")
    root.geometry("900x1000")  # 창 크기

    # 텍스트 출력
    Label(
        root,
        text=formatted_text,
        wraplength=750,  
        justify="left",  # 왼쪽 정렬
        anchor="w",  # 위쪽 왼쪽 정렬
        padx=10,
        pady=10
    ).pack()

    root.mainloop()
