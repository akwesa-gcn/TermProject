import pyautogui
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen():
    """
    화면 캡처 후 텍스트 추출
    """
    # 화면 캡처
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)

    # OpenCV로 이미지 변환
    screen_rgb = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

    # Tesseract를 사용한 OCR 텍스트 추출
    screen_text = pytesseract.image_to_string(screen_rgb, lang='eng+kor')  # +'언어'를 통해 추출하고싶은 언어 추가 가능
    return screen_text

