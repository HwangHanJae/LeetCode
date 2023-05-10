class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        number = 1
        while number <= n:
            if number == n:
                return True
            number *= 3
        else:
            return False
            