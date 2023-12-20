import pyautogui
import pyperclip
import time
from datetime import datetime, timedelta
import webbrowser

#pip3 install pyautogui
#pip3 install pyperclip
#pip3 install pynput

#pip install Pillow
def openChrome(page):
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    # "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    webbrowser.get(chrome_path).open(page,new=new)



#mouse
def getcurrentPosition():
    pyautogui.position()
    print(pyautogui.position())

def moveMouse(x,y,durationMs=1000):
    duration = durationMs/1000
    pyautogui.moveTo(x, y, duration)

def moveMouseToSex(durationMs=0):
    duration = durationMs/1000
    pyautogui.moveTo(1300, 590, duration)

def moveMouseToName(durationMs=0):
    duration = durationMs/1000
    pyautogui.moveTo(998, 500, duration)

def moveMouseToDOB(durationMs=0):
    duration = durationMs/1000
    pyautogui.moveTo(800, 590, duration)

def moveMouseToPassportExpiry(durationMs=0):
    duration = durationMs/1000
    pyautogui.moveTo(998, 700, duration)

def moveMouseToSubmit(durationMs=0):
    duration = durationMs/1000
    pyautogui.moveTo(1049, 838, duration)

def leftClick():
    pyautogui.leftClick()

def rightClick():
    pyautogui.rightClick()

def scroll(scroll=-10):
    pyautogui.scroll(scroll)

#Keyboard
def delayTrigger(function, arg=None, sleep=200):
    sleepForMs(sleep)
    if (arg):
        function(arg)
    else:
        function()
    

def triggerKey(key):
    pyautogui.hotkey(key)

def triggerEnter():
    pyautogui.press("enter")

def triggerForceReload():
    pyautogui.hotkey('ctrl', 'shift', 'r')

def triggerIncognitoMode():
    pyautogui.hotkey('ctrl', 'shift', 'n')

def triggerNewTab():
    pyautogui.hotkey('ctrl', 't')

def triggerTab():
    pyautogui.hotkey('tab')

def triggerInspector():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def triggerInspectorNetworkStop():
    pyautogui.hotkey('ctrl', 'e')

def altTab():
    pyautogui.hotkey('alt', 'tab')

def triggerF6():
    pyautogui.hotkey('f6')

def triggerF5():
    pyautogui.hotkey('f5')

def triggerCopy():
    pyautogui.hotkey("ctrl", "c")

def triggerPaste(text=""):
    if (text != ""):
        pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

def triggerkeyIn(str):
    for i in range(len(str)):
        pyautogui.hotkey(str[i])
        sleepForMs(200)

def ctrlA():
    pyautogui.hotkey("ctrl", "a")

#process
def sleepForMs(ms=1000):
    print("sleep for " + str(ms) + "ms")

    sleepMs = ms/1000
    time.sleep(sleepMs)

def sleepTillTargetTime(hour=8, minute=0, second=0, microsecond=0):
    target_time = datetime.now().replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    current_time = datetime.now()
    time_difference = target_time - current_time
    sleep_seconds = time_difference.total_seconds()
    if sleep_seconds > 0:
        print(f"Sleeping for {sleep_seconds} seconds until {target_time}")
        time.sleep(sleep_seconds)
    else:
        print("The target time has already passed.")

def calendarWidgetSetDate(tar):
    curr = datetime.now().date()
    print(tar)
    print(curr)
    if (curr.year != tar.year):
        #set year
        key = 'left'
        if (tar.year > curr.year):
            key = 'right'
        times = abs(curr.year - tar.year)
        moveYearMultiple(key, times)

    if(curr.month != tar.month):
        #set month
        key = 'left'
        if (tar.month > curr.month):
            key = 'right'
        times = abs(curr.month - tar.month)
        moveMonthMultiple(key, times)

    if(curr.day != tar.day):
        #set day
        key = 'left'
        if (tar.day > curr.day):
            key = 'right'
        times = abs(curr.day - tar.day)
        moveDayMultiple(key, times)
    triggerEnter()

def moveDayMultiple(key, presses=1):
    #moveMonthMultiple("left", 10)
    for i in range(presses):
        pyautogui.hotkey("alt", key)

def moveMonthMultiple(key, presses=1):
    #moveMonthMultiple("left", 10)
    for i in range(presses):
        pyautogui.hotkey("shift", key)

def moveYearMultiple(key, presses=1):
    #moveYearMultiple("left", 10)
    for i in range(presses):
        pyautogui.hotkey("ctrl", key)


        