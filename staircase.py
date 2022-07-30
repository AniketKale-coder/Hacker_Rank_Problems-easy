def staircase(n):
    for i in range(0, n):
        # print((" "*abs((i+1)-n))+"#"*(i+1))
        print(f"{'#'*(i+1):>{n}}")
    for i in range(0, n, 2):
        # print((" "*abs((i+1)-n))+"#"*(i+1))
        print(f"{'#'*(i+1):^{n}}")


# n = int(input("Enter No"))
n = 5

staircase(n)
