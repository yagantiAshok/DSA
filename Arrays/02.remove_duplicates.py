

"196. Remove duplicates from sorted array"

def remove_duplicates(array):

    "empty and single element array always unique so checking new element with previous"
    if len(array)==0:
        return 0 ,array
    previous_element = array[0]
    pos = 1
    for j  in range(1,len(array)):
        if array[j]!=previous_element:
            array[pos] = array[j]
            previous_element = array[j]
            pos = pos + 1
    return pos, array
res = remove_duplicates([0,0,0,3,3,3,5,6])
print(res)