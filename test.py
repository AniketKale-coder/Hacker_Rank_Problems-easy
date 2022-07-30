def diamat(arr):
    rd = 0
    ld = 0

    for i in range(len(arr)):
        ld += arr[i][i]
        return ld

    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i+j == len(arr)-1):
                rd += arr[i][j]
                return rd

    print(abs(rd-ld))


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]],
diamat(arr)
