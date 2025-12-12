#count of perfect square between 1 to n
N=int(input("enter a number "))
count=0
for i in range(1,N+1):
    if i*i<=N:
        count=count+1
        print(i*i,"",end="")
    else:
        break
print("\n",count)        