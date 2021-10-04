import subprocess
import os
import pyautogui
import time

# choice = print("Please choose the meeting program, Teams/Zomm: ")

meeting_id = "203 254 9339"
meeting_pass = input("Pleas input the meeting password: ")
duration = time.sleep(5)
#https://zoom.us/j/99699671480?pwd=VlB1OHA3RGhVaStiRDUxbHk0S1lPQT09
#Barzani Jawi is inviting you to a scheduled Zoom meeting.

Topic: Barzani Jawi's Personal Meeting Room

Join Zoom Meeting
https://zoom.us/j/2032549339?pwd=RitjVmxUNjhPNVJrMktHbW0vcXFUdz09

Meeting ID: 203 254 9339
Passcode: V4PXct


# Running Zoom first.
user_path = os.path.join(os.path.join(os.environ['USERPROFILE']))
zoom_path = user_path.replace("\\","/") +"/AppData/Roaming/Zoom/bin/Zoom.exe"
os.startfile(zoom_path)
print(zoom_path)
time.sleep(10)

# Locating join button.
join_btn = pyautogui.locateCenterOnScreen("join_btn.png", grayscale=True, confidence=.5)
pyautogui.moveTo(join_btn)
pyautogui.click(join_btn)
pyautogui.press('enter',interval=1)
pyautogui.typewrite(meeting_id)
for i in range(3):
    pyautogui.press("tab", interval=.01)
for i in range(2):
    pyautogui.press('space', interval=.5)
    pyautogui.press("tab", interval=.01)
pyautogui.press('space',interval=.5)
time.sleep(3)
pyautogui.typewrite(meeting_pass)
pyautogui.press("tab", interval=.01)
pyautogui.press('enter',interval=1)

# Recording
time.sleep(1)
pyautogui.hotkey("win" , "alt" , "r")
pyautogui.hotkey("win" , "alt" , "m")
duration()
# time.sleep(5)

# Stop recording
pyautogui.hotkey("win" , "alt" , "r")
time.sleep(1)


# Recording path
recording_path = user_path.replace("\\","/") + "/Videos/Captures"
os.startfile(recording_path)





# import schedule
# import time
# import webbrowser
#

# def open_link(link):
#     webbrowser.open(link)
#
# def demo_meeting():
#     open_link('MY ZOOM MEETING URL')
#
# schedule.every().friday.at("12:25").do(demo_meeting)
#
# while 1:
#     schedule.run_pending()
#     time.sleep(1)
