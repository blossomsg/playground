from math import cbrt

s = "test" # string
i = -1 # integer
i2 = -1 +2 # arithmetic expression

# print(s, f"\n{i}", f"\n{i2}")

def trial_func():
    return "this works"

def trial_func2(args):
    return args

def trial_func3(*args):
    return sum(args)

def trial_func4(**kwargs):
    return kwargs

def trial_func5(**kwargs):
    return pow(**kwargs)

def trial_func6(*args):
    return args

# print(trial_func(), trial_func2("\nthis works with args"), f"\n{trial_func3(1, 3, 10)}", f"\n{trial_func4(trial=888, trial2=564)}", f"\n{trial_func5(base=2, exp=4)}", f"\n{trial_func6("value1", "value2")}")

squares = [pow(x, 2) for x in range(10000)] # list comprehension
squares_g = tuple(pow(x, 2) for x in range(10000)) # generators comprehension
# print(squares)
# print(squares_g)

a = [1, 2, 3, 4, 5]
b = a
b.append(15)
# print(b)

def deco(func):
    def inner(*args):
        print(sum(args))
    return inner

@deco
def regular_print(*args):
    print(pow(args[0], args[1]))

# regular_print(8, 2)

class Biped:
    def __init__(self, name=None, kind=None, behaviour=None):
        self.name = name
        self.kind = kind
        self.behaviour = behaviour

    def __str__(self):
        return f"name: {self.name}, kind:{self.kind}, behaviour: {self.behaviour}"

    def __repr__(self):
        return f"name: {self.name}", f"kind:{self.kind}", f"behaviour: {self.behaviour}"

    @staticmethod
    def static(some_value):
        return some_value

    @classmethod
    def human(cls):
        return cls(name="Blossom", kind="Human", behaviour="Helpful")

    @classmethod
    def animal(cls):
        return cls(name="Kanga", kind="Animal", behaviour="Cruel")

    @classmethod
    def alien(cls):
        return cls(name="Ally", kind="Alien", behaviour="Shy")


# print(Biped.alien())
# print(Biped().static("this is a static test"))

# hashing same value - coursera
while True:
    txt = input("Enter a string: ")
    if len(txt) < 1 : break

    hv = 0
    pos = 0
    for let in txt:
        pos = ( pos % 3 ) + 1
        # print(pos)
        # print(ord(let))
        hv = (hv + (pos * ord(let))) % 1000000
        print(let, pos, ord(let), hv)

    print(hv, txt)

# eg modulo
# https://discuss.python.org/t/unintended-space-in-new-line-solved/51140/10
v1 = 10 % 3
v2 = 64 % 8
v3 = 18 % 3
v4 = 25 % 6
v5 = 172 % 3
# print(v1,v2, v3, v4, v5, sep="\n") # returns the remainder of division

