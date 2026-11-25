n=int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(f"{j}",end="")
    print()
