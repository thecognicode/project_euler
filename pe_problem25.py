def fibon(n):
    if n <= 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)

while True:
    if len(fibon(n)) == 4:
        print(n)

print(fibon(12))
for i in range(13):
    print(fibon(i), end=",")
# n = 1000
# print(len(str(n)))