class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [i for i in s]
        t = [i for i in t]
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in t:
                t.remove(s[i])

        if len(t) != 0:
            return False
        else:
            return True

