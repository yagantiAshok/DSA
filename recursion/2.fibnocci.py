


def fibnocci(num):

    if (num==1):

        return 1
    
    if (num==0):

        return 0
    
    ans = fibnocci(num-1) + fibnocci(num-2)

    return ans 


print(fibnocci(2))