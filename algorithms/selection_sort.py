import sys

def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                  
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [1,2,3,1,2,4,5,6,1,2,4]

print(selection_sort(arr))
