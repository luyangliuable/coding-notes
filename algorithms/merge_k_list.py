import random
import time

def merge_k_list(arr: list[list[int]]) -> list[int]:
    """
    Parameters:
        arr: list of lists containing integers of lengthk

    Returns:
        res: merged list of integers from original list of length k
    Author: Luyang Liu
    Date Written: 2022-03-14
    """
    res = []

    lengths = [len(each_arr) for each_arr in arr]

    total_length = sum(lengths)

    # TODO change instead of splicing using array to keep track of starting position
    for _ in range(total_length):
        current = 0
        current_lowest = arr[current][0]
        for j, each_arr in enumerate( arr ):
            if each_arr[0] < current_lowest:
                current = j
                current_lowest = each_arr[0]

        arr[current] = arr[current][1:]
        if [] in arr:
            arr.remove([])

        res.append(current_lowest)

    return res

# arr = [[1,2,5,6,7], [3,6,9,10,11]]
k = 5
arr = []
for _ in range(k):
    a = [random.randint(0,9)]
    print(a)
    for i in range(5):
        a.append(a[i] + random.randint(0,9))
    arr.append(a)

print(arr)

print("merging k is", str(len(arr)))
[print("arr", i+1, "is", each_arr) for i, each_arr in enumerate(arr)]
print("merged array is", merge_k_list(arr))
