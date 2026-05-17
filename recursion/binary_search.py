


def binarysearchrecursion(array,target,start,end):

    if (start > end ):

        return - 1
    
    middle = start + (end-start)//2

    if array[middle]==target:

        return middle
    
    elif array[middle]<target:

        start = middle + 1 #return binarysearchrecursion(array,target,middle+1,end)

    else:

        end = middle - 1   #return binarysearchrecursion(array,target,start,middle-1)

    return binarysearchrecursion(array,target,start,end)


array = [3,4,5,6,7,8,9,10]

print(binarysearchrecursion(array,10,0,len(array)))



