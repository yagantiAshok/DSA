
"Moves Zeroes to end"

def move_zeroes_end(array):

    n = len(array)
    pos = 0
    for j in range(n):
        if array[j]!=0:
            array[pos] = array[j]
            pos = pos + 1
    while pos<n:
        array[pos] = 0
        pos = pos + 1
    return array
res = move_zeroes_end([0,0,0,0,1])
print(res)