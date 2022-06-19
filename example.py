from noise_generator import *

from time import sleep
from click import clear

if __name__ == '__main__':
    xx = 0
    yy = 0
    clear()
    while True:
        xx += 0.4
        yy += 1
        x = ""
        for i in range(yy, yy+10):
            for j in range(int(xx), int(xx)+20):
                x += "░" if (int(noise(i, j)) <= 3) else ("▒" if (int(noise(i, j)) <= 10) else "▓")
            x += "\n"
        print("\033[%d;%dH" % (0, 0))
        print(x)
        sleep(0.05)