


def roted_sorted_array_ascending(array,target):
    
    start = 0
    end =len(array)-1

    while start<=end:

        middle = start + (end-start)//2

        if array[middle]==target:

            return True
        
        if array[start]<=array[middle]:

            if array[start]<=target<array[middle]:

                end = middle -1
            else:
                start = middle+1

        else:

            if array[middle]<target<=array[end]:

                start = middle+1
            else:

                end = middle - 1

    return False



array = [7, 0,7,7,7,7]

target = 0

result = roted_sorted_array_ascending(array,target)

print(result)