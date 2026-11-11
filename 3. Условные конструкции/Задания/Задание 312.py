x = int(input())
y = int(input())
if x == 0 or y == 0:
    print("На оси")
elif x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
else:
    print("IV")