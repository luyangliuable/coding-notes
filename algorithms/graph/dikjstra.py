# Implement insertion sort
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

arr = [1, 2, 3, 1, 2, 5, 6, 7, 8, 9, 4, 10]
print(insertion_sort(arr))
