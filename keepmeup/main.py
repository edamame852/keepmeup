import time, pyautogui
import multiprocessing
import random
import argparse
import datetime

def dontsleep(lunch_mode=False, time_input=0):

    def pressingbuttons():
        down, up = random.randint(1, 15), random.randint(1, 15)
        pyautogui.press('volumedown')
        print(f'volumedown - rest for ({down}) sec(s)')
        time.sleep(down)
        pyautogui.press('volumeup')
        print(f'volumeup - rest for ({up}) sec(s)')
        time.sleep(up)
        return up+down

    if lunch_mode:
        while True:
            current_time = datetime.datetime.now().time()
            print(f"The time now is: {current_time}")
            if current_time >= datetime.time(12, 0) and current_time < datetime.time(13, 0):
                print("Lunch break! Pausing activity for 1 hour.")
                time.sleep(3600)
            else:
                pressingbuttons()
    elif time_input > 5:
        timer = (time_input - 5) * 60
        while timer > 0:
            print("I'm still running ~ Better than I ever did!")
            seconds_elpased = pressingbuttons()
            timer -= seconds_elpased
            if timer > 0:
                print(f"Logic will run for another {timer} seconds")
        print(f"Termining program :(")
    
    else:
        pressingbuttons()

def KeepUI(lunch_mode=False,time_input=0):
    p2 = multiprocessing.Process(target=dontsleep(lunch_mode, time_input))
    p2.start()
    return p2

def main():
    parser = argparse.ArgumentParser(
        prog='keepmeup',
        description='Wakey wakey :)')
    parser.add_argument('--lunch', help='times out during lunch', action=argparse.BooleanOptionalAction)
    parser.add_argument('--time', help='how long you want to stay up for (in minutes) (will always minus 5)', type=int)
    args = parser.parse_args()

    if args.lunch:
        print("Lunch mode enabled")
        print("Press ctrl+c to kill me")
        p1 = KeepUI(lunch_mode=True)
        p1.start()
    elif args.time:
        if args.time <= 5:
            p1 = KeepUI(time_input=args.time)
            p1.start()
            print(f"Program will stop NOW immediately")
            p1.terminate()
        else:
            print("Press ctrl+c to kill me")
            print(f"Program will stop in roughly {args.time-5} minute(s)")
            p1 = KeepUI(time_input=args.time)
            p1.terminate()
    else:
        print("Press ctrl+c to kill me")
        p1 = KeepUI()
        p1.start()

if __name__ == '__main__':
    main()