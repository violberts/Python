start_sum=float(input())
target_sum=float(input())
percent=float(input())
a=0
while start_sum<=target_sum:
    a+=1
    start_sum+=start_sum*percent/100/12
    print(f"{a} - {start_sum:.2f}")
