def fibon(n):
    if n <= 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)

n = 0

while True:
    if len(str(fibon(n))) == 4:
        break
    else: 
        n += 1
print(n)

# Test Code
# print(len(str(fibon(n))))
