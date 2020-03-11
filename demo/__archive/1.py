
def inn():
    pos = 0
    def go(step):
        # nonlocal pos
        return pos+step
    return go

p=inn()
print("a",p(2))
d=inn()
print("b",d(3))
print("b",d(3))
print("a",p(2))
print("b",d(3))
print("a",p(2))
print("a",p(2))
print("b",d(3))
print("b",d(3))