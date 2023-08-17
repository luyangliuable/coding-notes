import random

def DNF_quicksort(arr: list[int], lo, hi):

    if len(arr) == 1:
        return arr

    P = partition(arr, lo, hi)

    DNF_quicksort(arr, lo, P-1)
    DNF_quicksort(arr, P+1, hi)

def partition(arr: list[int], lo, hi) -> int:
    pivot = arr[random.randint(lo, hi)]
    print("pivot is", pivot)
    b1 = lo
    j = lo
    b2 = hi

    while j <= b2:
        print(arr[j], ',', pivot)
        if pivot > arr[ j ]:
            print("swap", arr[j], "with", arr[b2])
            arr[b2], arr[j] = arr[j], arr[b2]
            b2 -= 1

        elif pivot < arr[j]:
            print("swap", arr[j], "with", arr[b1])
            arr[b1], arr[j] = arr[j], arr[b1]
            b1 += 1
            j += 1

        else:
            print("pivot detected")
            j+=1

        print("b1", b1, "j", j, "b2", b2)

    print(arr)
    return j

arr = [3,2,5,5,8,1,3,4]
# DNF_quicksort(arr, 0, len(arr)-1)
partition(arr, 0, len(arr)-1)
print(arr)
# print(DNF_quicksort(arr, 0, len(arr)-1))

