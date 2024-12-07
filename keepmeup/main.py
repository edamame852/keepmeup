import PySimpleGUI as sg
import time, pyautogui
import multiprocessing
import random
import argparse

def dontsleep():
    while True:
        down,up =random.randint(1, 300),random.randint(1, 300)
        pyautogui.press('volumedown')
        print(f'volumedown - rest for ({down}) sec(s)')
        time.sleep(down)
        pyautogui.press('volumeup')
        print(f'volumedown - rest for ({up}) sec(s)')
        time.sleep(up)


def KeepUI():
    sg.theme('Dark')
    layout = [
        [sg.Text('Keep-Me-Up is now running.\nYou can keep it minised, and it will continue running.\nClose it to disable it.')]
    ]
    window = sg.Window('Keep-Me-Up', layout)
    
    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:
        event = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            if p2.is_alive():
                p2.terminate()
            break

def main():
    parser = argparse.ArgumentParser(
                    prog='keepmeup',
                    description='Keeps your computer up :)')
    parser.add_argument('--lunch', help='times out during lunch', action=argparse.BooleanOptionalAction)
    parser.add_argument('--time', help='how long you want to stay up for', type=int)
    args = parser.parse_args()
    if args["lunch"]:
        dontsleep()
    elif args["time"]:
        pass
    else:
        p1 = multiprocessing.Process(target = KeepUI)
        p1.start()