def roted_array_duplicatesa(array,target):

    start = 0
    end = len(array)-1

    while start <=end:

        middle = start + (end-start)

        if array[middle]==target:

            return True
        
        if array[start]==array[middle]==array[end]:

            start = start + 1
            end = end - 1

        elif array[start]<=array[middle]:

            if array[start]<=target<array[middle]:

                end = middle - 1

            else:

                start = middle + 1
        else:

            if array[middle]<target<=array[end]:

                start = middle + 1
            else:

                end = middle - 1

    return False


array = [1,0,1,1,1]
target = 0

result = roted_array_duplicatesa(array,target)

print(result)

