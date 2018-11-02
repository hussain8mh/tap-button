import pyautogui 

def handle_command(command):
    if command == "right":
        pyautogui.click(button='right')
    elif command == "left":
        pyautogui.click(button='left')
