

def min_roted_sorted_array(array):



    start = 0

    end = len(array)-1

    while start < end:

        middle = start + (end-start)//2

        # if duplicates

        if array[middle]==array[end]:

            end = end - 1

        elif array[middle]>array[end]:

            start = middle + 1

        else:

            end = middle
        
    return array[end]

    

result = min_roted_sorted_array([1,1,1,1,1,1,0,1,1,1])

print(result)