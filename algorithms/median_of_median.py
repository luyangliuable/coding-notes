def median_of_median(arr: list[int]) -> int:
    length = len(arr)
    medians = []
    if length <=5:
        for i in range(length):

            j = i - 1
            key = arr[i]

            while j >= 0 and key < arr[j]:
                arr[j-1] = arr[j]
                j -= 1

            arr[j+1] = key

        mid = length//2
        print("mid is", arr[mid])
        return [arr[mid]]
    else:
        splits = [num for num in range(0, length, 4)]
        if splits[-1] != length:
            splits.append(length)

        for i in range(1,len( splits )):
            splitted_array_shard = arr[splits[i-1]:splits[i]]
            medians = medians + median_of_median(splitted_array_shard)
        return medians

arr = [3,2,5,5,8,1,3,4]
print(median_of_median(arr))




