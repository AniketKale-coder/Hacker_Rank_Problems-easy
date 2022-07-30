def plusMinus(arr):
        z=0
        neg=0
        p=0
        l=len(arr)
        for i in arr:
                if(i==0):
                        z+=1                        
                if(i<0):
                        neg+=1                          
                if(i>0):
                        p+=1
        print(round((p / l),6), end=" ")
        print(round((neg / l),6), end=" ")
        print(round((z/ l),6), end=" ")               

arr = [1,2,3,-1,-5,0,0,0,3,-5,-6]

plusMinus(arr)