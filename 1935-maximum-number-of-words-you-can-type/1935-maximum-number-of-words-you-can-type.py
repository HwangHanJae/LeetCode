class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for word in words:
            for c in brokenLetters:
                if c in word:   
                    break
            else:
                count += 1
        return count