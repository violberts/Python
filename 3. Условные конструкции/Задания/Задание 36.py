d = int(input())
f = int(input())
i = int(input())
c =max(d,f,i)
a =min(d,f,i)
b =d+f+i-c-a
if a+b<=c or b+c<=a or a+c<=b:
    print("Не существует")
elif a**2 + b**2 == c**2:
    print("Прямоугольный")
elif a**2 + b**2 > c**2:
    print("Остроугольный")
elif  a**2 + b**2 < c**2:
    print("Тупоугольный")

