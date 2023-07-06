from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = deque(word1)
        word2  = deque(word2)
        result = ''
        while word1 or word2:
            if len(word1) > 0:
                p1 = word1.popleft()
            else:
                p1 = ''
                
            if len(word2) > 0:
                p2 = word2.popleft()
            else:
                p2 = ''
            result += (p1+p2)

            
        return result
        