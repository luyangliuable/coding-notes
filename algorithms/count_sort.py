import random
import time

def count_sort(dictionary: list[int], input_list: list[int]) -> tuple:

    # count array is used for counting
    count = [0]*len(dictionary)

    # pos array is used for position
    pos = [0]*len(dictionary)

    for i in input_list:
        count[i] += 1

    for i in range(len(dictionary)):
        pos[i] = sum(count[:i])

    temp = [0]*len(input_list)

    for i in range(len(input_list)):
        temp[pos[input_list[i]]] = input_list[i]
        pos[input_list[i]] += 1

    return count, pos, temp


dictionary=[0,1,2,3,4,5,6,7,8,9,10]
print(len(dictionary))
input = [ random.choice(dictionary) for _ in range(10) ]


print("going to count sort", input)
start = time.process_time()
result = count_sort(dictionary, input)[2]
end = time.process_time() - start
print("result:",  result)
print("result took", str(end) + "s", "to run")
