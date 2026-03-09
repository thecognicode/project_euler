p = 1000
s = 0

num =  2 ** p
# print(num)
while num > 0:
    sum += num % 10
    num //= 10
    # print(num)
print(sum) 