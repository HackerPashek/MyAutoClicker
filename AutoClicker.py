import sys
import keyboard
import pyautogui
import time

is_Clicking = False

def Click():
	global is_Clicking
	if not is_Clicking:
		is_Clicking = True
		print("On")
	else:
		is_Clicking = False
		print("Off")

def Quit():
	global is_Clicking
	is_Clicking = False
	print("Quit")
	sys.exit()

# Press "x" to turn on/off clicker.
# Press "q" to disactivate it.
keyboard.add_hotkey("x", Click)
keyboard.add_hotkey("q", Quit)

while True:
	if is_Clicking:
		pyautogui.click(button = "left") 
		time.sleep(0.01)