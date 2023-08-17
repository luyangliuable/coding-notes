def selection_sort(arr: list) -> list:
    res = arr

    for i in range(len(res)):
        min = i
        for j in range(i+1, len(res)):
            if res[j] < res[min]:
                min = j

        # Invariant says that the unsorted list contains the next smallest value
        res[min], res[i] = res[i], res[min]

    return res

print(selection_sort([1,2,23,2,3,1,2,3,4,5,7,8,8]))
