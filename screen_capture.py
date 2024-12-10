import pyautogui
import cv2
import numpy as np

def capture_screen():
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    return cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
