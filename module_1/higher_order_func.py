# composition function
def first(x):
    return x+2
def second(h, x):
    return h(x) * 2
print("composition: ",second(first,2))


# Closure function
def addx(x):
    def _(y):
        return x+y
    return _
add2 = addx(2)
add3 = addx(3)
print("Closure: ",add2(2), add3(4))

# curry function
def f(x,y):
    return x*y
def f2(x):
    def _(y):
        return f(x,y)
    return _
print(f2(2))
print("curry: ",f2(2)(3))