from platform import system

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


os = system()
if os == 'Linux' or os == 'Darwin':
    rw_LEFT = chr(27)+chr(91)+chr(68)
    rw_RIGHT = chr(27)+chr(91)+chr(67)
    rw_UP = chr(27)+chr(91)+chr(65)
    rw_DOWN = chr(27)+chr(91)+chr(66)
    rw_ESC = chr(27)
    rw_ENTER = chr(13)
    rw_CTRLC = chr(3)
    rw_BKSP = chr(127)
elif os == 'Windows':
    rw_LEFT = chr(224)+chr(75)
    rw_RIGHT = chr(224)+chr(77)
    rw_UP = chr(224)+chr(72)
    rw_DOWN = chr(224)+chr(80)
    rw_ESC = chr(27)
    rw_ENTER = chr(13)
    rw_CTRLC = chr(3)
    rw_BKSP = chr(8)
    import ctypes
    from ctypes import c_long, c_wchar_p, c_ulong, c_void_p

    class _COORD(ctypes.Structure):
        _fields_ = [
        ("X", ctypes.c_short),
        ("Y", ctypes.c_short)]

    class _SMALL_RECT(ctypes.Structure):
        _fields_ = [
            ("Left", ctypes.c_short),
            ("Top", ctypes.c_short),
            ("Right", ctypes.c_short),
            ("Bottom", ctypes.c_short)]

    class _CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        _fields_ = [
            ("dwSize", _COORD),
            ("dwCursorPosition", _COORD),
            ("wAttributes", ctypes.c_ushort),
            ("srWindow", _SMALL_RECT),
            ("dwMaximumWindowSize", _COORD)]


rw_ARROWS = [rw_LEFT,rw_RIGHT,rw_UP,rw_DOWN]
rw_SPECIALS = rw_ARROWS + [rw_ENTER,rw_ESC,rw_BKSP]

def cls():
    from subprocess import call
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        call('clear', shell = True)
    elif os == 'Windows':
        call('cls', shell = True)

def locate(x, y, text):
    import sys
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()
    elif os == 'Windows':
       import ctypes
       """Move cursor to position indicated by x and y."""
       value = (x + (y << 16))
       gHandle = ctypes.windll.kernel32.GetStdHandle (c_long (-11))
       ctypes.windll.kernel32.SetConsoleCursorPosition (gHandle, c_ulong(value))
       ctypes.windll.kernel32.WriteConsoleW (gHandle, c_wchar_p(text), c_ulong(len(text)), c_void_p(), None)

def _move(x,y):
    import ctypes
    buffer_info = _CONSOLE_SCREEN_BUFFER_INFO()
    gHandle = ctypes.windll.kernel32.GetStdHandle (c_long (-11))
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(gHandle, ctypes.byref(buffer_info))
    x += buffer_info.dwCursorPosition.X
    y += buffer_info.dwCursorPosition.Y
    value = (x + (y << 16))
    ctypes.windll.kernel32.SetConsoleCursorPosition (gHandle, c_ulong(value))

def goLeft(steps):
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        print(rw_LEFT*steps,end="",flush=True)
    elif os == 'Windows':
        _move(-steps,0)

def goRight(steps):
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        print(rw_RIGHT*steps,end="",flush=True)
    elif os == 'Windows':
        _move(steps,0)

def goUp(steps):
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        print(rw_UP*steps,end="",flush=True)
    elif os == 'Windows':
        _move(0,-steps)

def goDown(steps):
    from platform import system
    os = system()
    if os == 'Linux' or os == 'Darwin':
        print(rw_DOWN*steps,end="",flush=True)
    elif os == 'Windows':
        _move(0,steps)

def cleartrailing(newSentence,maxlen):
    print(newSentence+" "*(maxlen-len(newSentence)),end="",flush=True)
    goLeft(maxlen-len(newSentence))

def wrapper(text, indent=2, width=72):
    output = []
    lines = str(text).split("\n")
    for line in lines:
        words = line.split(" ")
        wrapped=""
        for word in words:
            if len(wrapped)+len(word)+1< width:
                wrapped += word+" "
            else:
                output.append(" "*indent + wrapped)
                wrapped = word+" "
        output.append(" "*indent + wrapped)
    return output

def doCommaSentence (somelist,lastword="and"):
    output = ""
    for item in somelist:
            output += item
            output += sepSign(item,somelist,lastword)
    return output

def sepSign(item, items,lastword="and"):
    if len(items)>1:
        if item == items[-2]: return " "+lastword+" "
    if len(items)>0:
        if item == items[-1]:return "."
    return ", "

def rawput(words=[]):
    userinput = Userinput()
    cpos = 0
    strlen =0
    fullstring = ""
    words.append(fullstring)
    vpos = len(words)-1
    while True:
        high = userinput.get()
        if len(high)==1:
            if ord(high) >31 and ord(high) < 127:
                strlen+=1
                fullstring = fullstring[:cpos]+high+fullstring[cpos:strlen]
                cpos+=1
                print(fullstring[cpos-1:strlen], end="",flush=True)
                goLeft(strlen-cpos)
        if high==rw_LEFT and cpos > 0:
            cpos-=1
            goLeft(1)
            #print(rw_LEFT, end='',flush=True)
        if high==rw_RIGHT and cpos <strlen:
            cpos+=1
            goRight(1)
            #print(rw_RIGHT, end='',flush=True)
        if high==rw_BKSP and cpos > 0 and strlen >0:
            cpos -=1
            strlen -=1
            fullstring = fullstring[:cpos]+fullstring[cpos+1:strlen+1]
            goLeft(1)
            print(fullstring[cpos:strlen]+" ", end="",flush=True)
            goLeft(strlen-cpos+1)
        if vpos == len(words)-1 : words[-1] = fullstring
        if high == rw_UP and vpos > 0:
            vpos -= 1
            fullstring = words[vpos]
            goLeft(cpos)
            cleartrailing(fullstring,40)
            cpos = len(fullstring)
            strlen = len(fullstring)
        if high == rw_DOWN and vpos < len(words)-1:
            vpos += 1
            fullstring = words[vpos]
            goLeft(cpos)
            cleartrailing(fullstring,40)
            cpos = len(fullstring)
            strlen = len(fullstring)
        if high==rw_ENTER:
            print()
            words[-1] = fullstring
            return fullstring,words

class Userinput:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    #def __call__(self): return self.impl()
    #def __repr__(self): return self.impl()

    def get(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import sys, tty, termios,os

    def __call__(self):
        import sys, tty, termios,os
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        #termios.tcsetattr(fd, termios.TCSANOW, old_settings)
        #print(old_settings)
        #pattern=[]
        pattern=''
        ch = ''
        try:
            os.set_blocking(fd,False)
            tty.setraw(fd)
            #while ch!='' or pattern ==[]:
            while ch!='' or pattern == '':
                ch = sys.stdin.read(1)
                if ch != '':
                    pattern += ch
                    #pattern.append(ord(ch))
        finally:
            os.set_blocking(fd,True)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            #if pattern == [3]:
            if pattern == rw_CTRLC:
                os.set_blocking(fd,True)
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                raise Exception("User ctrl+c breakout!")
            #print("jkjk")
            #print(ord(ch[0]))
        return pattern

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        pattern=''
        ch = msvcrt.getch()
        if ord(ch) == 224:
            ch = msvcrt.getch()
            pattern = chr(224)+chr(ord(ch))
        else:
            pattern = ch.decode('utf-8')
        if pattern == rw_CTRLC:
            raise Exception("User ctrl+c breakout!")
        return pattern


def _userinput():
    import sys, tty, termios,os,time
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    #termios.tcsetattr(fd, termios.TCSANOW, old_settings)
    #print(old_settings)
    #pattern=[]
    pattern=''
    ch = ''
    try:
        os.set_blocking(fd,False)
        tty.setraw(fd)
        #while ch!='' or pattern ==[]:
        while ch!='' or pattern == '':
            ch = sys.stdin.read(1)
            if ch != '':
                pattern += ch
                #pattern.append(ord(ch))
    finally:
        os.set_blocking(fd,True)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        #if pattern == [3]:
        if pattern == rw_CTRLC:
            os.set_blocking(fd,True)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            raise Exception("User ctrl+c breakout!")
        #print("jkjk")
        #print(ord(ch[0]))
    return pattern

"""
windows arrows,special keys

up 224,72
left 224,75
right 224,77
down 224,80
esc 27
backspc 8
ctrl+c 3

"""
