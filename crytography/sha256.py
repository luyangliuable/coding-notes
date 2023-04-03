from hashlib import sha256
import csv

def check_zeroes(s):
    zeroes = 0
    i = 0
    while i < len(s):
        if s[i] != str(0):
            break

        i += 1

    return i

def mine(s, padding=None, MAX_LOOP=10000):
    # req = '0'*padding
    max_zeroes = 0
    input = ""
    output = ""
    nounce = 0

    with open("result.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(MAX_LOOP):
            s1 = s + str(nounce)
            res = sha256(s1.encode('utf-8')).hexdigest()

            if check_zeroes(res) >= max_zeroes:
                input = s1
                output = res
                max_zeroes = check_zeroes(res)
                print(output)
                writer.writerow([ input, output ])

            nounce += 1

    return output

if __name__ == "__main__":
    a_string = 'this string holds important and private information'
    test = "001234"

    res = mine(a_string, 0, 100000000000)
    print(res)
