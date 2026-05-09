

def lowerbound(array,x):

    size = len(array) - 1

    lower_bound = len(array)

    start = 0

    end = size

    while start<=end:

        middle = start + (end-start)//2

        if array[middle]>=x:

            lower_bound = middle 

            end = middle - 1
        else:
            start = middle + 1

    return lower_bound

array = [3,5,8,15,19]

x = 9

result = lowerbound(array,x)

print(result)