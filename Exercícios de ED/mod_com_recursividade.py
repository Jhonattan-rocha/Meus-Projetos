def mod(a=0, b=0):
    if a == 0 or b == 1 or a == b:  # ou a / b is int
        return 0
    elif a < b:
        return a
    else:
        a = a - b
        return mod(a, b)


print(mod(10, 4))
