def canReachLast(stones):
    maxReach = 0

    for i in range(len(stones)):
        
        if i > maxReach:
            return False

        
        maxReach = max(maxReach, i + stones[i])

    return True

n = int(input("Enter number of stones: "))

print("Enter the jump values for each stone:")
stones = list(map(int, input().split()))

if n != len(stones):
    print("Error: Number of stones does not match input values")
else:
    if canReachLast(stones):
        print("YES, it is possible to reach the last stone.")
    else:
        print("NO, it is NOT possible to reach the last stone.")
