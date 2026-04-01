class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i in t:
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        return len(count) == 0