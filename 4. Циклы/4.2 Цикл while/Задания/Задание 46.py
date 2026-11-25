a=int(input())
b=int(input())
while a>b:
    if a%2==0 and a//2>=b:
        print(":2")
        a=a//2
    else:
        print("-1")
        a=a-1
