
"706. Intersection of two sorted arrays"

def intersection(array1,array2):

    i_length = len(array1)
    j_length = len(array2)
    i = 0
    j = 0
    inter = []
    while i<i_length and j<j_length:
        if array1[i]<array2[j]:
            i+=1
        elif array1[i]>array2[j]:
            j+=1
        else:
           inter.append(array2[j])
           i+=1
           j+=1
    return inter
res = intersection([1, 2, 2, 3, 3, 3], [2,3,3,4,5,7])
print(res)