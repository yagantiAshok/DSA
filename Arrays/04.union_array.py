

"713. Union of two sorted arrays"

def add(union,element):
    if len(union)==0 or union[-1]!=element:
        union.append(element)

def union_array(array1,array2):
    i_lenght = len(array1)
    j_length = len(array2)
    union = []

    i = 0
    j = 0
    while i<i_lenght and j<j_length:

        if array1[i]<array2[j]:
            add(union,array1[i])
            i+=1
        elif array1[i]>array2[j]:
            add(union,array2[j])
            j+=1
        else:
            # so both are equal  any one element we could add
            add(union,array2[j])
            i+=1
            j+=1
    while i<i_lenght:
        add(union,array1[i])
        i+=1
    while  j<j_length:
        add(union,array2[j])
        j+=1

    return union

res = union_array([2,2],[2,2])
print(res)

    