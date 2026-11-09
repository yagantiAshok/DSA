def rotate_left(array, k):
    n = len(array)

    if n <= 1:
        return array

    k = k % n

    def reverse(start, end):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)

    return array