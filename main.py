# *arg

def func(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(func(1, 2, 3, 4, 5))