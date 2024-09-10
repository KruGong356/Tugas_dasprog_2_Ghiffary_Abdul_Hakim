arr = list(map(int, input().split()))

x = int(input())  
y = int(input())  

for _ in range(y):
    temp = arr[-x:] 
    arr = temp + arr[:-x]  

d, e, f = map(int, input().split())

print(arr[d], arr[e], arr[f])