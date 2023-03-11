import pyautogui
from tools import connect, find_click

pyautogui.moveTo(1917, 1062)
pyautogui.click() 
pyautogui.moveTo(1920/2, 1080/2)
pyautogui.click(button="right")
find_click("img/displays.png")

connect(1)
connect(2)
connect(4)

find_click("img/close.png")