def kth_min(arr, k):
    cp_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            cp_arr.append([arr[i], arr[j]])

    print(cp_arr)

kth_min([1,2,3], 6)
