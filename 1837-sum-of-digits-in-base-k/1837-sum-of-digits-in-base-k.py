class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = ''
        while n >= k:
            n, r = divmod(n, k)
            result += str(r)
        result += str(n)
        return sum([int(i) for i in result])