import random

def binary_search(arr: list, key: int) -> int:
    low = 0
    high = len(arr)


    while low < high:
            mid = (high+low)//2
            mid_value = arr[mid]
            print(mid, mid_value)
            if low < len(arr) - 1:
                if mid_value == key:
                    return mid
                elif mid_value < key:
                    low = mid
                elif mid_value > key:
                    high = mid
            else:
                break
    return 0


test_arr = [1,2,3,4,5,6,7,8,9,12,23,24,25,30,32]

for _ in range(115):
    print("\n")
    index = random.randint(0, len(test_arr)-1)
    print("for random index", index)
    print("result", binary_search(test_arr, test_arr[index]))
