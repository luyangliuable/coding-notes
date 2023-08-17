import random

def get_digit(number: int, digit: int) -> int:
    # NOTE: digit starts from 0 which means first one from the left!
    return number // 10**digit % 10


def radix_pass(input_list: list[int], base, digit):
    counter = [0]*(base)

    pos = [0]*(base)
    # pos[0] = 1
    for i in range(len(input_list)):
        counter[get_digit(input_list[i], digit)] += 1

    for i in range(base):
        pos[i] = sum(counter[:i])

    temp = [0]*len(input_list)

    for i in range(len(input_list)):
        num = get_digit(input_list[i], digit)
        temp[pos[num]] = input_list[i]
        pos[num] += 1

    return temp


def radix_sort(input_list: list[int], base, digits):
    for digit in range(1, digits + 1):
        input_list = radix_pass(input_list, base, digit)
        print("for", str( digit ) + "th", "digit, the resulting sorted array is", input_list)


    return input_list


arr = [random.randint(1000,9999) for _ in range(10)]
print("sorting array", arr)
print(radix_sort(arr, 10, 4))
