def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = factorial(100)
sum = 0
while num:
    sum += num % 10
    num = num // 10
print(sum)