


# one thing i learned pivot ,minimum ,how many rotations are same patterns 
# 

def times_array_sorted(array):

    start = 0
    end = len(array)-1

    while start < end:

        middle = start + (end-start)//2

        if array[middle]==array[end]:

            end = end - 1

        elif array[middle] > array[end]:

            start = middle + 1
        
        else:

            end = middle
    
    return start 


print(times_array_sorted([13,14,15,16,3,6,9]))