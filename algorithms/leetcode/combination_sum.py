class Solution(object):
    def combinationSum(self, candidates, target):
        # :type candidates: List[int]
        # :type target: int
        # :rtype: List[List[int]]
        # Time limit exceeded. Try to use DP?

        def backtrack(f = 0, t = []):
            if sum(t) == target:
                r.append(t) # result appends unique combination of values that sum to target

            # Perform combination search of possible combos
            for i in range(f, len(candidates)):

                if i != f and candidates[i] == candidates[i-1]:
                    # Skip if the combo already exists from taking the previous value
                    continue

                # Get the max num of the num candidate[i] added before it is more than target
                new = t + [candidates[i]]

                # Get the maximum number of additional candidate[i] values and try combo that is less than target
                while True:
                    backtrack(i + 1, new)

                    if sum(new + [candidates[i]]) > target:
                        break

                    new = new + [candidates[i]]


        r = []

        n = []
        # Filter out values larger than target
        for c in candidates:
            if c <= target:
                n.append(c)

        candidates = n
        candidates.sort() # Python Tim sort

        backtrack()

        return r

a = Solution()
# print(a.combinationSum([2,3,6,7], 7))
# print(a.combinationSum([2,3,5], 8))
# print(a.combinationSum([], 8))
# print(a.combinationSum([26,21,39,38,24,16,30,7,5,4,9,29,8,35,3,17,19,11,34], 8))
print(a.combinationSum([38,13,39,37,20,11,24,40,21,19,25,12,16,23,30,26,36,29,10,33,35,31], 40))
