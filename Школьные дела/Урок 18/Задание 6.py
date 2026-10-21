from math import *

x = float(input())
t = float(input())
z = ((9 * pi * t + 10 * cos(x)) / (sqrt(t) - abs(sin(t)))) * exp(x)
print(f"{z:.2f}")