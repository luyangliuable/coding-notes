import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.data.append(val)
        self.index_map[val] = len(self.data) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        a = self.data[-1]
        index = self.index_map[val]
        self.data[index] = a
        self.index_map[a] = index
        self.data.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
    

if __name__ == '__main__':
    obj = RandomizedSet()
    obj.insert(3)
    obj.remove(1)
    obj.insert(2)
    obj.remove(9)
    print(obj.data)
    obj.getRandom()
