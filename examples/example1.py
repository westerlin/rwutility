from rwutility import *

import sys

#test()
def testfinal():
    userinput = Userinput()
    ptn=''
    while ptn!=rw_ENTER and ptn!=rw_ESC:
        ptn = userinput.get()
        if ptn not in rw_SPECIALS:
            print(ptn)

cls()
testfinal()