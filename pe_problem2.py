def fibon(n):
    if n <= 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)

limit = fibon(4000000)

for i in range(limit):
    if i % 2 == 0:
        sum += 