from collections import deque
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = deque()
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber-1, 26)
            result.appendleft(chr(r+65))
        
        return ''.join(list(result))