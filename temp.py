from colorsys import TWO_THIRD
from tkinter import Y


def one(z):
    x = int(input("enter 5 plz"))
    z = y+x
    return x


def tow(z):
    x = int(input("plz enter 4"))
    z = y+x
    return x

def default():
    print("不理解")
    return "不理解啊啊"

y = 10
z = 20
x=0
alpha = 0

switcher = {
    0: one,
    1: tow
}
switcher.get(alpha,default)()
print(x)