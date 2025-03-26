import random
import time
import pyautogui as pg

count = int(input() or 1000)

while count > 0:
    x = random.randint(500, 700)
    y = random.randint(100, 1000)
    time_to_wait = random.random() * 2

    print(time_to_wait)
    print(count)

    pg.moveTo(x, y, 1)
    time.sleep(time_to_wait)

    count = count - 1
