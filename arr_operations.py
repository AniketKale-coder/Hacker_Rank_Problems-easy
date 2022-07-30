from ast import While

arr = [2, 2, 5, 2, 3, 3, 1, 1]
n = len(arr)
op = 0

for i in range(n-1):
    if(arr[i] == -1):
        continue
    for j in range(i+1, n):
        if(arr[j] == -1):
            continue
        if(arr[i] != arr[j]):
            arr[i], arr[j], op = -1, -1, op+1
            break

for i in arr:
    op += 1 if i != -1 else 0

print(op)
