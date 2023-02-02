#!/usr/bin/python
# coding: latin-1

# Imports
from pynput import keyboard
import pyautogui as pg

ab = "qwertyuiopñljkhgfdsazxcvbnm"
abc = list(ab.upper()+ab)
num = list("1234567890")
extra_char = list('"`+*^´Ç}{[]- .:,;<>!|?¿¡#()$£%^&*!')
char = abc + num + extra_char

print('Press "G"')

def start():
    i = -1 ; i2 = 0 ; i3 = i2 ; i4 = i2 ; i5 = i2 ; i6 = i2 ; i7 = i2 ; i8 = i2 ; i9 = i2 ; i10 = i2 ; i11 = i2 ; i12 = i2 ; i13 = i2 ; i14 = i2 ; i15 = i2 ; i16 = i2
    Nl = int(len(char)) ; todo = ""
    RNl = Nl ** 16
    while i != RNl:
        todo = ""
        i += 1
        a = str(char[i])
        todo +=  str(a)
        pg.typewrite(todo+"\n")
        if True:
            if i == Nl-1:
                i2 += 1
                i = -1
            b = str(char[i2])
            todo +=  str(b)
            pg.typewrite(todo+"\n")
            if True:
                if i2 == Nl:
                    i3 += 1
                    i2 = -1
                c = str(char[i3])
                todo +=  str(c)
                pg.typewrite(todo+"\n")
                if True:
                    if i3 == Nl:
                        i4 += 1
                        i3 = 0
                    d = str(char[i4])
                    todo +=  str(d)
                    if True:
                        if i4 == Nl:
                            i5 += 1
                            i4 = 0
                        e = str(char[i5])
                        todo +=  str(e)
                        pg.typewrite(todo+"\n")
                        if True:
                            if i5 == Nl:
                                i6 += 1
                                i5 = 0
                            f = str(char[i6])
                            todo += str(f)
                            pg.typewrite(todo+"\n")
                            if True:
                                if i6 == Nl:
                                    i6 = 0
                                    i7 += 1
                                g = str(char[i7])
                                todo += str(g)
                                pg.typewrite(todo+"\n")
                                if True:
                                    if i7 == Nl:
                                        i8 += 1
                                        i7 = 0                    
                                    h = str(char[i8])
                                    todo += str(h)
                                    pg.typewrite(todo+"\n")
                                    if True:
                                        if i8 == Nl:
                                            i9 += 1
                                            i8 = 0
                                        j = str(char[i9])
                                        todo += str(j)
                                        pg.typewrite(todo+"\n")
                                        if True:
                                            if i9 == Nl:
                                                i9 = 0
                                                i10 += 1
                                            k = str(char[i10])
                                            todo += str(k)
                                            pg.typewrite(todo+"\n")
                                            if True:
                                                if i10 == Nl:
                                                    i10 = 0
                                                    i11 += 1
                                                m = str(char[i11])
                                                todo += str(m)
                                                pg.typewrite(todo+"\n")
                                                if True:
                                                    if i11 == Nl:
                                                        i12 += 1
                                                        i11 = 0
                                                    l = str(char[i12])
                                                    todo += str(l)
                                                    pg.typewrite(todo+"\n")
                                                    if True:
                                                        if i12 == Nl:
                                                            i12 = 0
                                                            i13 += 1
                                                        n = str(char[i13])
                                                        todo += n
                                                        pg.typewrite(todo+"\n")
                                                        if True:
                                                            if i13 == Nl:
                                                                i13 = 0
                                                                i14 += 1
                                                            o = str(char[i14])
                                                            todo += o
                                                            pg.typewrite(todo+"\n")
                                                            if True:
                                                                if i14 == Nl:
                                                                    i15 += 1
                                                                    i14 = 0
                                                                q = str(char[i15])
                                                                todo += q
                                                                pg.typewrite(todo+"\n")
                                                                if True:
                                                                    if i15 ==Nl:
                                                                        i16 += 1
                                                                        i15 = 0
                                                                    r = str(char[i16])
                                                                    todo += r
                                                                    pg.typewrite(todo+"\n")
        print(todo)
        todo = ""

def on_press(key):
    try:
        if str(key.char) == "g":
            start()
        else:
            print("Is not a letter g press g to strat")
    except:
        print("Is not a letter, press g to start")
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
