def calc(n):
    if n == 0:
        factorial = 1
    else:
        factorial = n * calc(n-1)
    return factorial

print(calc(5))