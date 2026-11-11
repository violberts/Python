a = int(input())
n = a%10
s = a%100
if 2<= n <=4 and s!= 12 and s!= 13 and s!= 14:
    print("гриба")
elif n == 1 and s != 11:
    print("гриб")
else:
    print("грибов")