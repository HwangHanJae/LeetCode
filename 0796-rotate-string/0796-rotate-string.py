from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        goal = deque(goal)
        count = 0
        while count < len(s):
            s = deque(s)
            p = s.popleft()
            s.append(p)
            count += 1
            if tuple(s) == tuple(goal):
                return True
        return False