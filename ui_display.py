from tkinter import Tk, Label

def show_summary(summary_text):
    root = Tk()
    root.title("화면 분석 결과")
    Label(root, text=summary_text, wraplength=400).pack(padx=20, pady=20)
    root.mainloop()
