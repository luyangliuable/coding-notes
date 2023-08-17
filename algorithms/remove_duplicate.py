import random
import merge_sort

def r_dup(arr: list[int]) -> list[int]:

    res = mergesort( arr )
    print("sorted is", res)

    # Sliding window
    i = 0
    previous = res[0]
    length = 1
    index = 1
    for i in range(1, len(res)):
        if res[i] != previous:
            length += 1
            previous = res[i]
            res[index] = res[i]
            index +=1

    return res[:length]


def mergesort(arr):
    res = arr
    if len(res) > 1:
        # Finding the mid of the resay
        mid = len(res)//2

        # Dividing the resay elements
        L = res[:mid]

        # into 2 halves
        R = res[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp resays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res[k] = L[i]
                i += 1
            else:
                res[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            res[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            res[k] = R[j]
            j += 1
            k += 1

    return arr


for _ in range(5):
    arr = [random.randint(0,100) for _ in range(10)]
    print("sorting and removing duplicate in", arr)
    print("The array without duplicates is", r_dup(arr))
