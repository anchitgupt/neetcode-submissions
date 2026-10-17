class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        from collections import Counter
        dist = Counter(nums)
        for num in dist:
            if dist[num] >= 2:
                return True
        return False  