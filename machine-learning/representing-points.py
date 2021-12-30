two_d = [10, 2]
five_d = [30, -1, 50, 0, 2]


four_d = [10,-2,5,10]


def euclidean_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
         distance += ( pt1[i] - pt2[i] )**2
    return distance ** 0.5 # math.sqrt(distance)


def manhattan_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
         distance += abs( pt1[i] - pt2[i] )
    return distance


def hamming_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
         if pt1[i] != pt2[i]:
             distance += 1
    return distance

print(euclidean_distance([1,2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))
# print(euclidean_distance([2,3,4], [1,2]))


print(manhattan_distance([1,2], [4,0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))

print(hamming_distance([1,2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))
