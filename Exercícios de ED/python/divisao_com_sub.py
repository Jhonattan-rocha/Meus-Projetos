def div(num, num2):
    if num == num2:
        return 1
    elif num < num2:
        return 0
    else:
        num -= num2
        return div(num, num2) + 1


print(div(4, 2))
