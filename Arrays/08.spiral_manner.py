

"107. Print the matrix in spiral manner"

def spiral_matrix(array):

    matrix = []
    rows = len(array) 
    columns = len(array[0]) 

    top = 0
    bottom = rows - 1
    left = 0
    right = columns - 1

    while top<=bottom and left<=right:

        # top elements
        for j in range(top,right+1):
            matrix.append(array[top][j])
        top+=1

        # right elements
        for j in range(top,bottom+1):
            print(j)
            matrix.append(array[j][right])
        right-=1

        # bottom elements
        if top<=bottom:
            for j in range(right,left-1,-1):
                matrix.append(array[bottom][j])
            bottom-=1

        # left elements
        if left<=right:
            for j in range(bottom,top-1,-1):
                matrix.append(array[j][left])
            left+=1

    return matrix


matrix = [
    [1],
    [2],
    [3],
    [4]
]

res = spiral_matrix(matrix)
print(res)


