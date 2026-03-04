# n = 100
# add = 0
# for i in range(1,n+1):
#     square = i ** 2
#     # print(square, end=' ')
#     if square % 2 != 0:
#         # print(square, end=' ')

#         add += square
# print(add)

# sum = 0
# for i in range(0, n+1):
#     if i % 2 != 0:
#         sum += i**2
# print(sum)

n = 100
square_sum = 0
sum_square = 0 
all_sum = 0

for i in range(1,n+1):
    square_sum += i ** 2
    all_sum += i
    sum_square = all_sum ** 2

# print(all_sum)
print(sum_square-square_sum)
