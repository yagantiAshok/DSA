



def kth_missing_number(arr,k):

    start = 0
    end = len(arr) - 1
    

    while start<=end:

        middle = start + (end-start)//2

        missing = arr[middle] - (middle+1)

        if missing<k:

            start = middle + 1

        else:

            end = middle - 1
    
    return start+k

arr = [2,3,5,8,10]
print(kth_missing_number(arr,1))
