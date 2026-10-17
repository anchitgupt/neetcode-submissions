class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s1 = Counter(s)
        t1 = Counter(t)

        if len(s1) != len(t1):
            return False    

        for let in set(s+t):
            if s1[let] != t1[let]:
                return False
        return True