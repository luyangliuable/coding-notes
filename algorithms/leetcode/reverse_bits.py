class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        num_of_bits = 32

        for i in range(num_of_bits):
            bit = (n >> i) & 1
            res |= bit << (num_of_bits - 1 - i)

        return res

if __name__ == "__main__":
    a = Solution()
    print(a.reverseBits(43261596))
