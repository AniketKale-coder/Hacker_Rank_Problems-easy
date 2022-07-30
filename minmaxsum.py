def miniMaxSum(arr):
    # Write your code here
    minnum = min(arr)
    maxnum = max(arr)
    minsum = sum(arr)-maxnum
    maxsum = sum(arr)-minnum
    print(minsum)
    print(maxsum)


arr = [1, 2, 3, 4, 5]
miniMaxSum(arr)
