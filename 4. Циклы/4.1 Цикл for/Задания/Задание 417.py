n = int(input())
zeros = 0
negative = 0
positive = 0
c = 0
for i in range(n):
    a=int(input())
    if a==0:
        zeros+=1
    if a<0:
        negative+=1
    if a>0:
        positive+=a
        c+=1
sr=positive/c
print("Нулей:", zeros)
print("Отрицательных:", negative)
print(f"Среднее положительных: {sr:.2f}")



