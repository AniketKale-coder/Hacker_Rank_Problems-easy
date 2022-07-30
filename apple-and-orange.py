def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    home_apples = [a + i for i in apples]
    home_oranges = [b + i for i in oranges]

    for _a in home_apples:
        if(s <= _a <= t):
            apples_count += 1
    for _b in home_oranges:
        if(s <= _b <= t):
            oranges_count += 1

    # for i in range(s, t+1):
    #     res = i in home_apples
    #     if(res == True):
    #         apples_count += 1

    # for i in range(s, t + 1):
    #     res = i in home_oranges
    #     if(res == True):
    #         oranges_count += 1

    print(f"apples:{home_apples}")
    print(f"apples:{apples_count}")
    print(f"oranges:{home_oranges}")
    print(f"oranges:{oranges_count}")


apples = [-2, 2, 1]
oranges = [5, -6]
a = 3
b = 2
s = 7
t = 11
result = countApplesAndOranges(s, t, a, b, apples, oranges)
