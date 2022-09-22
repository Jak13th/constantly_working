import pyautogui
import time
import os

os.environ['DISPLAY'] = ':0'

def const_work():
    while True:
        pyautogui.moveTo(100, 100)
        time.sleep(1)
        pyautogui.moveTo(200, 100)
        pyautogui.moveTo(200, 200)
        pyautogui.moveTo(100, 200)
        time.sleep(10)

if __name__=='__main__':
    const_work()