N = int(input())
status = True
for i in range(2,N):
    if(N%i == 0):
        status = False
        break
if(status):
    print("it is a prime")
else:
    print("it is not a prime")