import time

def f2(func):
    print(time.time())
    func()

def f1():
    print("dec")

f2(f1)