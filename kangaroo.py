def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 > x2 and v1 > v2:
        return "NO"
    elif x1 < x2 and v1 < v2:
        return "NO"
    if(v1 == v2):
        return "NO"
    if((x2-x1) % (v1-v2) == 0) and ((x2-x1) % (v2-v1) == 0):
        return "YES"
    else:
        return "NO"


x1 = 0
v1 = 3
x2 = 4
v2 = 2

result = kangaroo(x1, v1, x2, v2)
print(result)
