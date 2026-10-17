class Solution:
    def isPalindrome(self, s: str) -> bool:

        ls = ''.join(s.lower())
        ls = [s for s in ls if s.isalnum()]
        f,l=0,len(ls)-1

        while f<l:
            if ls[f] != ls[l]:
                return False
            f+=1
            l-=1
            
        return True