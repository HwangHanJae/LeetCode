class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for jewel in jewels:
            result += stones.count(jewel)
            
        return result