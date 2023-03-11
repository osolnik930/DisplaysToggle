import pyautogui
import time
from def_vals import *

def find_click(fname):
    location = None
    while location == None:
        location = pyautogui.locateOnScreen(fname, confidence=CONFIDENCE)
    pyautogui.moveTo(location)
    pyautogui.click()

def scroll(val):
    pyautogui.scroll(val)
    time.sleep(SCROLL_SLEEP_TIME)

def connect(monitor):
    find_click(f"img/{monitor}c.png")
    scroll(-1000)
    find_click("img/disconnect.png")
    find_click("img/extend.png")
    find_click("img/keepchanges.png")
    scroll(1000)

def disconnect(monitor):
    find_click(f"img/{monitor}.png")
    scroll(-1000)
    find_click("img/extend.png")
    find_click("img/disconnect.png")
    find_click("img/keepchanges.png")
    scroll(1000)