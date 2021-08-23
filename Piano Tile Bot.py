import time
import keyboard
import pyautogui
import win32api
import win32con
import sys


def find_cords_and_colour():
    cords = ('cords',)
    position = pyautogui.position()
    x = position[0]
    y = position[1]

    RGB = ('RGB',)
    colours = pyautogui.pixel(int(x), int(y))
    r = (colours,)
    cords_and_colour = cords + position + RGB + r
    print(cords_and_colour)


def click(x, y):  # click function
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.02)


print(
    'Press F4 to see your coordinates and RGB value'
    '\nHold F8 to begin inputs once you know your 4 x coordinates, 1 y coordinate '
    'and RGB value for colour you want to click')

while True:
    if keyboard.is_pressed('F4'):
        find_cords_and_colour()
        time.sleep(1)
    if keyboard.is_pressed('F8'):
        break

# if ycord != '':
#    while keyboard.is_pressed('F4') == False:
#       if pyautogui.pixel(-1158, 620) [0] == 0:
#            click(-1158, 620)
#       if pyautogui.pixel(-1028, 620) [0] == 0:
#           click(-1028, 620)
#       if pyautogui.pixel(-896, 620) [0] == 0:
#           click(-896, 620)
#       if pyautogui.pixel(-768, 620) [0] == 0:
#           click(-768, 620)

if keyboard.is_pressed('F8'):
    first = int(input('What is x cord of column 1?'))
    second = int(input('What is x cord of column 2?'))
    third = int(input('What is x cord of column 3?'))
    fourth = int(input('What is x cord of column 4?'))
    ycord = int(input('What is y cord of columns?'))
    red_value = int(input('What is the first RGB value when doing F4 on a black tile?'))
    print(' Press console key to start \n Press Esc to stop script')

    keyboard.wait('`')

    while True:
        if pyautogui.pixel(first, ycord)[0] == red_value:
            click(first, ycord)
            print("clicked 1")

        if pyautogui.pixel(second, ycord)[0] == red_value:
            click(second, ycord)
            print("clicked 2")

        if pyautogui.pixel(third, ycord)[0] == red_value:
            click(third, ycord)
            print("clicked 3")

        if pyautogui.pixel(fourth, ycord)[0] == red_value:
            click(fourth, ycord)
            print("clicked 4")

        if keyboard.is_pressed("Esc"):
            print('You ended script')
            time.sleep(3)
            sys.exit()

# 1 -1158 646
# 2 -1028 640
# 3 -896 640
# 4 -768 636
