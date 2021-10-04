# Teams-Zoom-Bot
# This code will help you to automatically join and record meetings for both Zoom and Teams. 

# Code
import os
import sys
import time
import schedule
import pyautogui
import selenium
import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




choice = input("Please choose the meeting program, Teams/Zoom: ")
duration = int(input("Please input the duration of the meeting in seconds. 1 Hour = 3600 sec: "))
meeting_time = str(input("Please input the meeting time (e.g 11:30): "))
print("#"*90)
print("This process takes around 20 sec, please do not interrupt it once it started.".center(90,"#"))
print("#"*90)
time.sleep(2)

path = os.path.join(os.path.join(os.environ['USERPROFILE']))


if choice.upper() == "TEAMS":
    link = input("Please copy the invitation link and paste it here: :")

elif choice.upper() == "ZOOM":
    meeting_id = input("Please input the meeting ID: ")
    meeting_pass = input("Please input the meeting password: ")
else:
    print(f"Your choice didn't match any documents, make sure the answer is spelled correctly, exiting...")
    time.sleep(5)
    sys.exit()


def program():
    if choice.upper() == "TEAMS":
        return True
    elif choice.upper() == "ZOOM":
        return False
    else:
        print(f"Your choice didn't match any documents, make sure the answer is spelled correctly, exiting...")
        time.sleep(5)
        sys.exit()



# For Teams meetings.
def teams():
    if program() == True:
        print(" Strating Teams..")
        teams_path = path.replace("\\", "/") + "/AppData/Local/Microsoft/Teams/current/Teams.exe"
        os.startfile(teams_path)
        time.sleep(10)

        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-extensions')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        driver.get(link)
        driver.find_element_by_xpath('//*[@id="buttonsbox"]/button[3]').click()
        time.sleep(1)

        pyautogui.press("tab", interval=.01)
        pyautogui.press("tab", interval=.01)
        pyautogui.press('space', interval=1)
        pyautogui.press("tab", interval=.01)
        pyautogui.press('space', interval=1)
        pyautogui.press("tab", interval=.01)
        pyautogui.press("tab", interval=.01)
        pyautogui.press('space', interval=1)
        for i in range(4):
            pyautogui.press("tab", interval=.01)

        pyautogui.press('space', interval=1)
        pyautogui.hotkey('win', 'up', interval=1)
        os.system("taskkill /f /im chrome.exe")
        recording()
    else:
        return(None)



# For Zoom meetings.
def zoom():
    if program() == False:
        print("Starting Zoom..")
        zoom_path = path.replace("\\", "/") + "/AppData/Roaming/Zoom/bin/Zoom.exe"
        os.startfile(zoom_path)
        time.sleep(10)

        join_btn = pyautogui.locateCenterOnScreen("join_btn.png", grayscale=True, confidence=.5)
        pyautogui.moveTo(join_btn)
        pyautogui.click(join_btn)
        pyautogui.press('enter', interval=1)
        pyautogui.typewrite(meeting_id)
        for i in range(3):
            pyautogui.press("tab", interval=.01)
        for i in range(2):
            pyautogui.press("tab", interval=.01)
            pyautogui.press('space', interval=.5)

        time.sleep(3)
        pyautogui.typewrite(meeting_pass)
        pyautogui.press("tab", interval=.01)
        pyautogui.press('enter', interval=1)
        pyautogui.hotkey('win', 'up')
        recording()
    else:
        return(None)


def recording():
# Start recording
    time.sleep(1)
    pyautogui.hotkey("win", "alt", "r")
    pyautogui.hotkey("win", "alt", "m")
    time.sleep(duration)

# Stop recording
    pyautogui.hotkey("win", "alt", "r")
    time.sleep(1)

# Recording path.
    recording_path = path.replace("\\", "/") + "/Videos/Captures"
    os.startfile(recording_path)
    time.sleep(3)
    print("Successfully completed the sequences, exiting...")
    time.sleep(3)
    sys.exit()



schedule.every().day.at(meeting_time).do(teams)
schedule.every().day.at(meeting_time).do(zoom)

while True:
    schedule.run_pending()
    print(f"Order confirmed, initializing starting sequence at {meeting_time}")
    time.sleep(5)



