N=int(input("enter the number of elements :"))
arr=[]
for i in range (0,N):
    e=int(input("enter the number :"))
    arr.append(e)
K=int(input("enter the target sum:"))    
i=0
while i<=N-1:
    j=i
    curr_sum=0
    while j<=N-1:
        curr_sum=curr_sum+arr[j]
        if curr_sum==K:
            print("Target subarray found from index",i,"to",j)
            exit(0)
        j=j+1
    i=i+1
print(-1,-1)    
    
