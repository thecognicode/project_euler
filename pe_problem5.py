s = 1
n = 20

while s >= 1: 
    for i in range(1,n+1):
        if s % i != 0:
            break
    else:
        print(s)
        break
    s += 1
