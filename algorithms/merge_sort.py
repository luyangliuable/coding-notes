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
  
arr = [12,3,2,2,1,2,3,3,4,5,6,7,8,8,9,9,4,31,2]
mergesort(arr)
print(arr)
