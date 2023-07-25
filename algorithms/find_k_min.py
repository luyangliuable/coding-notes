import random

def find_k_min(arr: list[int], k: int) -> list[int]:
    min_stack = []
    temp_stack = []
    min_stack.append( arr[0] )

    for i in range(1, len(arr)):
        current = arr[i]

        if(len(min_stack)) < k:
            min_stack.append(current)
        else:
            max_val = min_stack.pop()
            for i in range(len( min_stack )):
                popped_val = min_stack.pop()

                if popped_val > max_val:
                    temp_stack.append(max_val)
                    max_val = popped_val
                else:
                    temp_stack.append(popped_val)
            if max_val > current:
                temp_stack.append(current)
            else:
                temp_stack.append(max_val)


            for i in range(len(temp_stack)):
                min_stack.append(temp_stack.pop())

    return min_stack


for _ in range(10):
    arr = [random.randint(0,99) for _ in range(10)]
    print("finding min of", arr)
    print("min is", find_k_min(arr, 4))
