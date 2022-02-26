def mod(a=0, b=0):
    if a / b is int:
        return 0
    elif a < b:
        return a
    else:
        a = a - b
        return mod(a, b)


print(mod(9, 4))
