#!/bin/python3
# this program will print out the notes from Code with harry website into a pdf file

import webbrowser,pyautogui,time

# This function will be used to print the page
def printPage():
    pyautogui.hotkey("ctrl","p");
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(10)    

url = "https://www.codewithharry.com/videos/javascript-tutorials-in-hindi-{}"


for i in range(1,67):

    webbrowser.open(url.format(i));
    time.sleep(5);
    printPage();
    time.sleep(7)

