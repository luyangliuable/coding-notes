def b(arr, t):
    l = 0
    r = len(arr) - 1

    while l<=r:
        m = (l+r)//2

        if arr[m] < t:
            l = m + 1
        elif arr[m] < t:
            r = m - 1
        else:
            return m

    return None

if __name__ == '__main__':
    print(b([1,2,3, 5, 6, 7, 8], 8))
