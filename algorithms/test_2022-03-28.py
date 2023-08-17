from collections import ChainMap
from itertools import cycle
import codecs

a = cycle("ABCD")

counter = 0
for i in a:
    print(i)
    if counter == 10:
        break
    counter += 1

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day4': 'Thu'}

res1 = ChainMap(dict1, dict2)
print(res1.maps,'\n')

res2 = ChainMap(dict2, dict1)
print(res2.maps,'\n')
