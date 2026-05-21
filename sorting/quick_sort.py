


def partition(l1,start,end):

    pivot = end

    count = 0

    for i in range(start,end):

        if l1[i]<l1[pivot]:

            count = count + 1
        
    count = count + start
    
    l1[count],l1[pivot] = l1[pivot], l1[count]


    i = start

    j = end 

    while (i<count) and (j>count):

        if l1[i]<l1[count]:

            i = i + 1
        
        elif l1[j]>=l1[count]:

            j = j - 1

        else:

            l1[i],l1[j] = l1[j],l1[i]

            i = i + 1
            j = j - 1

    return count 

l1 = [8,4,1,9,3,7,2,5,-1,4,4,4,9,1,100]

def quicksort(l1,start,end):

    if (start>=end):
        return 
    
    pivot_index = partition(l1,start,end)

    quicksort(l1,start,pivot_index-1)
    quicksort(l1,pivot_index+1,end)


print(quicksort(l1,start=0,end=len(l1)-1))

print(l1)