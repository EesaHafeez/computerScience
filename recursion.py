def calc(n):
    if n == 0:
        factorial = 1
    else:
        factorial = n * calc(n-1)
    return factorial

print(calc(5))

def calcSum(n):
    i = 0
    sum = 0
    while i <= n:
        sum = sum + i
        i = i +1
    return sum
print(calcSum(10))


def calc(n):
    if n == 0:
        sum = 0
    else:
        sum = n + calc(n-2)
    return sum
print(calc(2))