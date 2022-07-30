# Program to display the Fibonacci sequence up to n-th term

def fib(nterms):
    n1, n2 = 0, 1
    n = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while n < nterms:
            print(n1)
            fibseries = [].append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            n += 1
    return fibseries


nterms = int(input("How many terms? "))

# first two terms

fibseries = []
result = fib(nterms)
print(result)
# check if the number of terms is valid
