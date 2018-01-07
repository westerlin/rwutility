from rwutility import *

import sys

#test()
def testfinal():
    userinput = Userinput()
    ptn=''
    while ptn!=rw_ENTER and ptn!=rw_ESC:
        #old_settings = termios.tcgetattr(sys.stdin.fileno())
        #tty.setraw(sys.stdin.fileno())
        ptn = userinput.get()
        #os.set_blocking(sys.stdin.fileno(),True)
        #termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
        if ptn not in rw_SPECIALS:
            print(ptn)

cls()
sys.stdout.write(RESET)
testfinal()

#getch.clear()

import time
import sys
import os

def countd():

    seconds = 59
    minutes = 4
    five_minutes = 0

    os.system('clear')

    while five_minutes != 300:
        sys.stdout.write("%d:%02.f\r" % (minutes, seconds))
        sys.stdout.flush()
        seconds -= 1
        if seconds == -1:
            minutes -= 1
            seconds = 59

        five_minutes += 1
        time.sleep(1)
