class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        cnt = s.count(letter)
        n = len(s)
        result = int((cnt / n) * 100)
        return result