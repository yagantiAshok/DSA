



def peak_element(array):


    start = 0
    end = len(array) - 1

    while start < end:

        middle = start + (end-start)//2

        if array[middle] < array[middle+1]:

            start = middle + 1
        
        else:

            end = middle

    return start 
        

print(peak_element([3,2,6,5,3]))