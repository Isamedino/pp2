# 1

def squares(n):
    i = 0
    while i <= n:
        yield i ** 2
        i += 1

N = int(input())
for square in squares(N):
    print(square)




# 2
def even_numbers(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input("введите n "))
even_nums = even_numbers(n)

print(*even_nums, sep=", ")




# 3
def div34(n):
    for i in range(n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

n=int(input())
for num in div34(n):
    print(num)



# 4

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a=int(input())
b=int(input())
for num in squares(a,b):
    print(num)



# 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n=int(input())
for num in countdown(n):
    print(num)