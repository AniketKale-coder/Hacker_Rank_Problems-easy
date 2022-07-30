def fac(a, b):
    for n in a:
        for i in range(1, n+1):
            if i % n == 0:
                res = i


a = [2, 4]
b = [16, 32, 96]

result = fac(a, b)
