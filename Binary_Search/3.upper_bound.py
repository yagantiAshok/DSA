



def upperbound(array,x):

    size = len(array) - 1

    upperbound = len(array)

    start = 0

    end = size

    while start<=end:

        middle = start + (end-start)//2

        if array[middle]>x:

            upperbound = middle 

            end = middle - 1

        elif array[middle]<=x:

            start = middle + 1

    return upperbound

array = [0,3,5,8,9,15,19]

x = 0

result = upperbound(array,x)

print(result)