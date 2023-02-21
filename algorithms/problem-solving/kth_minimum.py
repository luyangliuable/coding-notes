def kth_min(arr, k):
    cp_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            cp_arr.append([arr[i], arr[j]])

    cp_arr.sort()

    print(cp_arr)
    return cp_arr[k-1]

print(kth_min([1,2,3], 7))
