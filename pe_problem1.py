n = 100

add = 0
sum_squares = 0
squares_sum = 0

for i in range(0, n+1):
    sum_squares += i ** 2
    add += i
    squares_sum = add ** 2

print(squares_sum - sum_squares)    
# print(sum_squares)
# print(squares_sum)

