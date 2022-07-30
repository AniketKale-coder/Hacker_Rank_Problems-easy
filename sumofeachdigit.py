def getSum(n):
    # sumdigit=0
    # if(m==0):
    #     print(m)
    #     return 0
    # if(m%9==0):
    #     print(m)
    #     return 9
    # else:
    #     print(m)
    #     return m%9

    #     for i in str(m):
    #         sumdigit+=int(i)
    #         m=str(sumdigit)
    # s= sum(list(map(int,list(str(n)))))
    s=0
    while(n!=0):
        s+=n%10
        n=n//10

    return s if s<10 else getSum(s)
    
n=12345
# m=2**n
result=getSum(n)
print(result)
