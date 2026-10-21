from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
print(a + b + c, S)
