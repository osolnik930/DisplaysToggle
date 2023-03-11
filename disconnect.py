import pyautogui
from tools import disconnect, find_click

pyautogui.moveTo(1917, 1062)
pyautogui.click() 
pyautogui.moveTo(1920/2, 1080/2)
pyautogui.click(button="right")
find_click("img/displays.png")

disconnect(1)
disconnect(2)
disconnect(4)

find_click("img/close.png")