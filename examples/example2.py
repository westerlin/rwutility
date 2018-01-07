import sys,os
from rwutility import *

cls()

words = ["stop","examine tree","go through door","throw spear","open chest"]

while True:
    print("What do you want? ",end="",flush=True)
    yourcommand,words = rawput(words)
    print(" >> ECHO : {}".format(yourcommand))

print(yourcommand)

def test():
    for line in sys.stdin.read(1):
        print(ord(line))
        print(line)
