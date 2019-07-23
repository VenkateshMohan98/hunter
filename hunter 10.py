V,K=map(int,input().split())
lis1=list(input().split())
lis2=list(input().split())
if set(lis2) <= set(lis1):
    print("YES")
else:
    print("NO")
