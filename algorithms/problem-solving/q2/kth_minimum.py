def getkthSmallestTerm(arr, k):
    a = []

    if len( arr ) == 0:
        return []

    # Check which first number
    f_idx = k // len(arr)

    # Get the second term index
    s_idx = k - f_idx*len(arr) - 1

    # Count number of f_idx numbers
    c = 0

    for i in range(len(arr)):
        if arr[i] == arr[f_idx-1]:
            c += 1

    for i in range(f_idx-1, f_idx+c-1):
        for j in range(len(arr)):
            a.append([arr[i], arr[j]])

    a.sort()
    print(a)

    r = a[s_idx]

    if r[1] > r[0]:
        return [r[1], r[0]]

    return r

# 1,2 1,2 2,1 2,1 2,2 2,2
cp_arr = [2, 2, 1]
cp_arr2 = [4, 1]
print(getkthSmallestTerm(cp_arr, 5))
print(getkthSmallestTerm(cp_arr2, 3))
