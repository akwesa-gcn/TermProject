import cv2
import numpy as np
import pygetwindow as gw  # 특정 창 캡처에 사용

def capture_screen():
    screen = np.array(gw.getWindowsWithTitle("YourWindowName")[0])
    return cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
