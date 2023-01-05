import time
import os
import sys

# Colors
class warna:
    reset = "\033[0m"
    yellow = "\033[1;33m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    cyan = "\033[1;36m"

os.system("clear")

def load1():
    load = [warna.yellow + "\n\n\t\t.", ":", ":", "S", "e", "d", "a", "n", "g",  " ", "M", "e", "n", "d", "o", "w", "n", "l", "o", "a", "d", ":", ":", ".\n" + warna.reset]
    for c in load:
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(0.1)

def load2():
    print ("\t\t =======================")
    load = [warna.cyan + "\t\t▁", " ▂", " ▃", " ▄", " ▅", " ▆", " ▇", " █", " ", "1", "0", "0", "%\n\n" + warna.reset]
    for c in load:
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(0.1)

if __name__=='__main__':
    load1()
    load2()
