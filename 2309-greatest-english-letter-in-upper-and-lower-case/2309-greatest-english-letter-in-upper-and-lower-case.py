class Solution:
    def greatestLetter(self, s: str) -> str:
        result = ""
        for c in s:
            if c.upper() in s and c.lower() in s:
                if c.upper() > result:
                    result = c.upper()
        return result