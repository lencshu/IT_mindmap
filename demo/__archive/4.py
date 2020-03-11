import time

def f3(a):
    print(a)
    def f2(func):
        # print(a)
        def wrapper(*arg):
            print(time.time())
            func(*arg)
        return wrapper
    return f2

@f3("good")
def f1(*a):
    print("dec",*a)

# f2(f1)("aaa","asd")
f1("aaa",'asdad')