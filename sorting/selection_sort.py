


def selection_sort(array):

    for i in range(len(array)-1):
        
        small_element = i

        for j in range(i+1,len(array)):

            if array[j]<array[small_element]:

                small_element = j

        if small_element!=i:

            array[i],array[small_element]=array[small_element],array[i]

    return array


result = selection_sort([45,1,34,100,-1,0])
print(result)