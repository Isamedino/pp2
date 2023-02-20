import math

#1 
n = int(input())

print((n * math.pi)/180)


#2 
h = int(input("высота: "))
x = int(input("значие х: "))
y = int(input("значение у: "))

print((x + y)/2 * h)

#3

n = int(input("количество сторон: "))
a = int(input("длина стороны: "))

print(int((n*a ** 2)/(4 * math.tan(math.pi/n))))


#4

x = int(input())
y = int(input())
print(x * y)


