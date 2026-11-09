

" Find missing number"

def find_missing_number(array):

    for i in range(len(array)+1):
        if i not in array:
            return i
res = find_missing_number([0, 1, 2, 4, 5, 6])
print(res)

"  s = n(n+1)/2 "